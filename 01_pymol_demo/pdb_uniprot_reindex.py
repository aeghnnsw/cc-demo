#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "biopython>=1.80",
# ]
# ///
"""
PDB to UniProt Residue Re-indexing Tool

This tool aligns PDB sequences to UniProt sequences and re-indexes PDB residues
to match the UniProt numbering, standardizing visualization across structures.

Usage with uv:
    uv run pdb_uniprot_reindex.py --pdb input.pdb --uniprot-file sequence.fasta --output output.pdb
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from Bio import Align
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import re


@dataclass
class ResidueMapping:
    """Mapping between PDB and UniProt residue numbering"""
    pdb_resnum: int
    uniprot_resnum: int
    residue_type: str
    chain: str


class PDBUniProtReindexer:
    """Main class for re-indexing PDB residues to match UniProt sequences"""
    
    def __init__(self):
        self.aligner = Align.PairwiseAligner()
        self.aligner.match_score = 2
        self.aligner.mismatch_score = -1
        self.aligner.open_gap_score = -2
        self.aligner.extend_gap_score = -0.5
    
    def parse_pdb_sequence(self, pdb_file: str) -> Dict[str, List[Tuple[int, str]]]:
        """Extract sequence and residue numbers from PDB file"""
        sequences = {}
        
        with open(pdb_file, 'r') as f:
            for line in f:
                if line.startswith('ATOM') and line[12:16].strip() == 'CA':
                    chain = line[21]
                    resnum = int(line[22:26])
                    resname = line[17:20].strip()
                    
                    if chain not in sequences:
                        sequences[chain] = []
                    
                    # Convert 3-letter to 1-letter amino acid code
                    aa_code = self.three_to_one(resname)
                    if aa_code:
                        sequences[chain].append((resnum, aa_code))
        
        return sequences
    
    def three_to_one(self, three_letter: str) -> Optional[str]:
        """Convert 3-letter amino acid code to 1-letter"""
        conversion = {
            'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
            'GLU': 'E', 'GLN': 'Q', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
            'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
            'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'
        }
        return conversion.get(three_letter)
    
    def parse_uniprot_sequence(self, sequence: str) -> str:
        """Parse UniProt FASTA sequence"""
        # Remove header line if present
        lines = sequence.strip().split('\n')
        if lines[0].startswith('>'):
            sequence_lines = lines[1:]
        else:
            sequence_lines = lines
        
        return ''.join(sequence_lines)
    
    def align_sequences(self, pdb_seq: str, uniprot_seq: str) -> Tuple[str, str, float, int]:
        """Align PDB and UniProt sequences using local alignment"""
        # Configure for local alignment
        self.aligner.mode = 'local'
        self.aligner.match_score = 2
        self.aligner.mismatch_score = -1
        self.aligner.open_gap_score = -2
        self.aligner.extend_gap_score = -0.5
        
        alignments = self.aligner.align(uniprot_seq, pdb_seq)
        best_alignment = alignments[0]
        
        # Get alignment strings
        alignment_str = str(best_alignment)
        lines = alignment_str.split('\n')
        uniprot_aligned = lines[0]
        pdb_aligned = lines[2]
        
        # Calculate identity percentage
        matches = sum(1 for a, b in zip(uniprot_aligned, pdb_aligned) 
                     if a == b and a != '-')
        identity = matches / len(pdb_seq) * 100
        
        # Get the start position in UniProt sequence
        uniprot_start = best_alignment.aligned[0][0][0] if len(best_alignment.aligned[0]) > 0 else 0
        
        return uniprot_aligned, pdb_aligned, identity, uniprot_start
    
    def create_residue_mapping(self, pdb_residues: List[Tuple[int, str]], 
                              uniprot_aligned: str, pdb_aligned: str, uniprot_start: int) -> List[ResidueMapping]:
        """Create mapping between PDB and UniProt residue numbers"""
        mappings = []
        uniprot_pos = uniprot_start  # Start from the alignment start position
        pdb_idx = 0
        
        for i, (uniprot_aa, pdb_aa) in enumerate(zip(uniprot_aligned, pdb_aligned)):
            if uniprot_aa != '-':
                uniprot_pos += 1
            
            if pdb_aa != '-':
                if pdb_idx < len(pdb_residues):
                    pdb_resnum, residue_type = pdb_residues[pdb_idx]
                    
                    # Only map if alignment matches
                    if uniprot_aa == pdb_aa and uniprot_aa != '-':
                        mapping = ResidueMapping(
                            pdb_resnum=pdb_resnum,
                            uniprot_resnum=uniprot_pos,
                            residue_type=residue_type,
                            chain='A'  # Default chain
                        )
                        mappings.append(mapping)
                    
                    pdb_idx += 1
        
        return mappings
    
    def reindex_pdb(self, input_pdb: str, output_pdb: str, mappings: List[ResidueMapping]):
        """Create new PDB file with re-indexed residue numbers"""
        # Create mapping dictionary for quick lookup
        mapping_dict = {m.pdb_resnum: m.uniprot_resnum for m in mappings}
        
        with open(input_pdb, 'r') as infile, open(output_pdb, 'w') as outfile:
            for line in infile:
                if line.startswith(('ATOM', 'HETATM')):
                    old_resnum = int(line[22:26])
                    if old_resnum in mapping_dict:
                        new_resnum = mapping_dict[old_resnum]
                        # Replace residue number (columns 23-26, 1-indexed)
                        new_line = line[:22] + f'{new_resnum:4d}' + line[26:]
                        outfile.write(new_line)
                    else:
                        outfile.write(line)  # Keep original if not in mapping
                else:
                    outfile.write(line)
    
    def generate_report(self, mappings: List[ResidueMapping], identity: float, 
                       output_file: str):
        """Generate alignment and mapping report"""
        with open(output_file, 'w') as f:
            f.write("# PDB to UniProt Re-indexing Report\n\n")
            f.write(f"## Alignment Statistics\n")
            f.write(f"- Sequence Identity: {identity:.1f}%\n")
            f.write(f"- Residues Mapped: {len(mappings)}\n\n")
            
            f.write("## Residue Mapping\n")
            f.write("| PDB ResNum | UniProt ResNum | Residue | Chain |\n")
            f.write("|------------|----------------|---------|-------|\n")
            
            for mapping in mappings[:20]:  # Show first 20 mappings
                f.write(f"| {mapping.pdb_resnum} | {mapping.uniprot_resnum} | "
                       f"{mapping.residue_type} | {mapping.chain} |\n")
            
            if len(mappings) > 20:
                f.write(f"| ... | ... | ... | ... |\n")
                f.write(f"| (showing first 20 of {len(mappings)} mappings) | | | |\n")
    
    def process_structure(self, pdb_file: str, uniprot_sequence: str, 
                         output_pdb: str, report_file: str) -> bool:
        """Main processing function"""
        try:
            # Parse PDB sequence
            print("Parsing PDB sequence...")
            pdb_sequences = self.parse_pdb_sequence(pdb_file)
            
            if not pdb_sequences:
                print("ERROR: No sequences found in PDB file")
                return False
            
            # Use first chain (typically chain A)
            chain = list(pdb_sequences.keys())[0]
            pdb_residues = pdb_sequences[chain]
            pdb_seq = ''.join([aa for _, aa in pdb_residues])
            
            print(f"PDB sequence ({len(pdb_seq)} residues): {pdb_seq[:50]}...")
            
            # Parse UniProt sequence
            uniprot_seq = self.parse_uniprot_sequence(uniprot_sequence)
            print(f"UniProt sequence ({len(uniprot_seq)} residues): {uniprot_seq[:50]}...")
            
            # Align sequences
            print("Aligning sequences...")
            uniprot_aligned, pdb_aligned, identity, uniprot_start = self.align_sequences(pdb_seq, uniprot_seq)
            
            print(f"Sequence identity: {identity:.1f}%")
            print(f"Alignment starts at UniProt position: {uniprot_start + 1}")
            
            if identity < 90:
                print(f"WARNING: Low sequence identity ({identity:.1f}%). Results may be unreliable.")
            
            # Create residue mapping
            print("Creating residue mapping...")
            mappings = self.create_residue_mapping(pdb_residues, uniprot_aligned, pdb_aligned, uniprot_start)
            
            print(f"Mapped {len(mappings)} residues")
            
            # Reindex PDB file
            print(f"Creating re-indexed PDB file: {output_pdb}")
            self.reindex_pdb(pdb_file, output_pdb, mappings)
            
            # Generate report
            print(f"Generating report: {report_file}")
            self.generate_report(mappings, identity, report_file)
            
            return True
            
        except Exception as e:
            print(f"ERROR: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Re-index PDB residues to match UniProt sequence numbering",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pdb_uniprot_reindex.py --pdb 7kxo.pdb --uniprot-file BTK_sequence.fasta --output 7kxo_reindexed.pdb --work-dir ./01_PL_BTK/work
  python pdb_uniprot_reindex.py --pdb structure.pdb --uniprot-file sequence.fasta --output reindexed.pdb
        """
    )
    
    parser.add_argument('--pdb', required=True, help='Input PDB file')
    parser.add_argument('--uniprot-sequence', help='UniProt sequence (FASTA format text)')
    parser.add_argument('--uniprot-file', help='UniProt sequence file (FASTA format)')
    parser.add_argument('--output', required=True, help='Output re-indexed PDB file')
    parser.add_argument('--report', help='Output report file (default: output.md)')
    parser.add_argument('--work-dir', help='Working directory for output files (creates subdirectories)')
    
    args = parser.parse_args()
    
    # Validate inputs
    if not Path(args.pdb).exists():
        print(f"ERROR: PDB file not found: {args.pdb}")
        sys.exit(1)
    
    # Get UniProt sequence
    uniprot_sequence = None
    if args.uniprot_sequence:
        uniprot_sequence = args.uniprot_sequence
    elif args.uniprot_file:
        if not Path(args.uniprot_file).exists():
            print(f"ERROR: UniProt file not found: {args.uniprot_file}")
            sys.exit(1)
        with open(args.uniprot_file, 'r') as f:
            uniprot_sequence = f.read()
    else:
        print("ERROR: Must provide either --uniprot-sequence or --uniprot-file")
        sys.exit(1)
    
    # Handle working directory structure
    if args.work_dir:
        work_dir = Path(args.work_dir)
        # Create subdirectories
        pdb_dir = work_dir / "pdb_files"
        reports_dir = work_dir / "reports"
        pdb_dir.mkdir(parents=True, exist_ok=True)
        reports_dir.mkdir(parents=True, exist_ok=True)
        
        # Update output paths to use working directory structure
        output_filename = Path(args.output).name
        args.output = str(pdb_dir / output_filename)
        
        if not args.report:
            base_name = Path(output_filename).stem
            args.report = str(reports_dir / f"{base_name}_reindex_report.md")
    else:
        # Set default report file with standardized naming
        if not args.report:
            # Extract base name without extension
            base_name = Path(args.output).stem
            # Create report filename: {base_name}_reindex_report.md
            args.report = f"{base_name}_reindex_report.md"
    
    # Process structure
    reindexer = PDBUniProtReindexer()
    success = reindexer.process_structure(args.pdb, uniprot_sequence, args.output, args.report)
    
    if success:
        print("\n✅ Re-indexing completed successfully!")
        print(f"📄 Re-indexed PDB: {args.output}")
        print(f"📊 Report: {args.report}")
    else:
        print("\n❌ Re-indexing failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()