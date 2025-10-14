# BTK Structure Visualization Task

Please create a PyMOL visualization of BTK kinase structure 8FLL following these steps, ensure you create a folder under 01_pymol_demo and put all intermediate and results file in the folder

1. Read `BTK_review.md` to understand BTK structure and important features

2. Download and prepare structure 8FLL:
   - Download the PDB file
   - Use `pdb_uniprot_reindex.py` to reindex the PDB file to match UniProt sequence numbering
   - Need to use uv run to run the reindex script

3. Create PyMOL visualization highlighting the key structural features of BTK:
   - Show different BTK domains and any important features you identify from the review
   - Display and label important residues that are critical for BTK function
   - Include any additional features you think are important to visualize
   - Use selection for each important motif or key residues to group before visualize

   Visualization requirements:
   - Label font size: 24 and bold
   - Use Spring Pastels color palette: ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7"]
   - Remove water molecules and non-ligand heteroatoms, for example SO4
   - For the ligand: use colored carbon atoms and stick representation
   - For key residues use line view
   - Use white background

4. Capture multiple snapshot images that best showcase the structure and its key features
   - No need to ray, just capture is enough
   - Need to zoom in or adjust depth to make sure the view is clear
   - Show or hide relevant labels before capturing the view to only show relevant informations


5. Create an HTML visualization report (`BTK_8FLL_visualization.html`) that includes:
   - The captured images
   - Legends explaining the color scheme and labeled residues
   - Important information about this structure and its features

Other notes
   - No need to save pymol session as pse
