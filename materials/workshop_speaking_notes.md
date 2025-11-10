# AI for Research Workshop - Speaking Notes
**Date:** November 10, 2025
**Presenter:** Shen Wang @ ChengLab
**Audience:** Graduate Students

---

## Overall Workshop Introduction (5 minutes)

**Opening:**
"Good morning/afternoon everyone! Welcome to our AI for Research workshop. My name is Shen Wang from the Cheng Lab, and I'm excited to share with you how AI tools, specifically Claude Code, can dramatically accelerate your research workflows.

Before we dive in, let me ask: How many of you have used AI assistants like ChatGPT or Claude for your research? [wait for response] Great! And how many have found yourself limited by what these tools can do - like not being able to access real-time data, run calculations, or interact with your specialized software? [wait for response]

That's exactly what we'll address today. This workshop is about transforming AI from a conversational assistant into a true research partner that can actually DO things - access databases, run molecular modeling software, automate your data collection pipelines, and much more.

We're going to cover four main topics today: the Model Context Protocol that connects AI to external tools, subagents that help manage complex multi-step tasks, skills that provide specialized workflows, and GitHub integration best practices. By the end of this workshop, you'll understand how to extend AI capabilities to match your specific research needs."

---

## Slide 2: Outline

**Transition:**
"Let's look at our agenda for today. [gesture to slide]

We'll start with the **Model Context Protocol** - this is the foundation that lets AI connect to external systems. Think of it as teaching your AI assistant how to use tools.

Next, we'll explore **Subagents and Automation** - these are specialized AI workers that can tackle complex, multi-step tasks independently while keeping your main conversation clean.

Then we'll discuss **Skills** - pre-packaged workflows and expertise that you can invoke whenever needed.

Finally, we'll cover **GitHub Integration and Best Practices** - because reproducibility and collaboration are crucial in research.

Throughout the workshop, we'll have several live demos and I encourage you to ask questions at any point. We'll also have discussion periods where I'd love to hear about your specific use cases."

---

## Slide 3: Model Context Protocol (MCP)

**Introduction to concept:**
"Let's start with the Model Context Protocol, or MCP for short.

[read slide] MCP is an open-source standard that connects AI applications to external systems.

Now, what does that really mean? Look at this diagram. On the left, we have AI applications - like Claude Code. On the right, we have all sorts of external resources: databases, computational tools, and entire workflows. MCP sits in the middle as a standardized bridge.

The beautiful thing about MCP being a *standard* is that you write your connection once, and it works with any AI application that supports MCP. You're not locked into a single vendor or tool.

For researchers, this is incredibly powerful because your specialized tools - whether it's PyMOL for molecular visualization, VASP for quantum calculations, or your custom data analysis scripts - can now be directly accessible to AI. The AI doesn't just talk about your research - it can actually participate in it."

---

## Slide 4: AI Agents Need Tools

**Emphasize the analogy:**
"Here's a fundamental insight: AI agents need tools, just like humans use calculators.

Think about it - you wouldn't do a complex statistical analysis in your head, right? You use software. Similarly, AI models are incredibly intelligent, but they have limitations that tools can overcome.

Let's look at three key categories: [point to each column]

**Real-time Data** - AI models have a knowledge cutoff date. They don't know today's weather, current stock prices, or the latest papers published last week. But with MCP tools, they can fetch this information in real-time. For you as researchers, this means accessing up-to-date literature databases, current experimental data, or real-time instrument readings.

**Taking Action** - By themselves, AI models can only generate text. They can't modify your files, send emails, or schedule your compute jobs. But with tools, they become active participants in your workflow. They can edit your code, submit batch jobs, or even update your lab notebook.

**Specialized Expertise** - And this is where it gets really exciting for research. We can give AI access to domain-specific tools: molecular modeling software, scientific computing libraries, specialized literature databases. The AI becomes fluent in your specific research domain.

The key insight here is that AI plus tools is far more powerful than AI alone. It's not just about conversation anymore - it's about action."

---

## Slide 5: PyMOL-MCP Demo

**Setup for demo:**
"Now let's see this in action with a live demo. I'm going to show you PyMOL-MCP - a connection between Claude and PyMOL, the molecular visualization software many of you probably use.

[Prepare to switch to demo]

What's remarkable here is that I can have a natural conversation with Claude about protein structures, and Claude will directly manipulate PyMOL to show me what I'm asking about.

Watch as I ask Claude to fetch a protein structure, analyze binding sites, color specific regions, and create visualizations - all through natural language, without me typing a single PyMOL command.

[Conduct demo - suggested prompts:]
- 'Fetch ubiquitin (1UBQ) and show me the structure'
- 'Highlight the alpha helices in blue and beta sheets in red'
- 'Find and show potential binding pockets'
- 'Create a publication-quality image from this angle'

[After demo]
Notice how I didn't need to remember PyMOL syntax? I just described what I wanted, and the AI translated that into precise PyMOL commands. This is the power of combining AI's language understanding with tool access."

---

## Slide 6: Building Your Own MCP

**Practical guidance:**
"Now you might be thinking - that's great for PyMOL, but what about MY tools? And that's the best part - you can build your own MCP connections.

The philosophy here is simple: **Anything with an API can become MCP tools.**

Let me give you two approaches: [point to columns]

**Start Using MCP** - The fastest way to get started is to search for existing MCP servers. The Model Context Protocol organization on GitHub has a growing collection. There are already MCP servers for:
- File systems
- Databases (PostgreSQL, SQLite)
- Git operations
- Web search
- Slack, Google Drive
- And many more

My recommendation: install a few, experiment with them, and iterate. Let the AI help you configure and use them.

**Build Your Own** - But for your specialized research tools, you might need to build custom MCPs. Here's the approach:
1. Identify which API or function you want to wrap
2. Keep your MCP functions simple - don't over-engineer
3. Let AI handle the intelligence - your MCP just needs to execute
4. And here's a secret: AI can help you code the MCP itself!

The barrier to entry is much lower than you think. A basic MCP server can be just 50-100 lines of Python code.

**Discussion question:** [pause for engagement]
What APIs or tools in your research workflow would you want to connect to AI? Think about:
- Lab equipment with APIs?
- Computational software you use regularly?
- Databases you frequently query?
- Custom scripts you've written?

[Allow 2-3 responses and briefly discuss feasibility]"

---

## Slide 7: Subagents

**Define the concept:**
"Let's move on to our second major topic: Subagents.

So what is a subagent? [read slide] Subagents are specialized AI assistants for specific tasks.

Here's the key thing to understand: [point to each bullet]

**Separate context windows** - Each subagent has its own conversation thread. This means it can go deep into a complex task without cluttering your main conversation. Imagine you're having a high-level discussion about your research approach, but you need someone to go analyze 50 data files in detail. You don't want all that analysis in your main thread - you just want the results. That's what subagents do.

**Task-specific design** - We can create subagents optimized for particular jobs: code review, debugging, data analysis, literature search. Each one has specialized instructions and knowledge for its domain.

**Custom tools and permissions** - Different subagents can have access to different tools. Your code review agent might be read-only, while your file processing agent can write and modify files.

**Automatic or explicit invocation** - Some subagents activate automatically when they detect relevant tasks. Others you call explicitly by name.

For researchers, think of subagents as your lab group - you have specialists for different tasks who can work semi-independently."

---

## Slide 8: Complex Tasks Need Specialized Experts

**Connect to research reality:**
"Why do we need subagents? Because complex tasks need specialized experts.

In your lab, you don't have one person do everything, right? You have people who specialize in synthesis, characterization, modeling, data analysis. Subagents work the same way.

Let me explain three key benefits: [point to each column]

**Context Management** - This is huge. When you're working on a complex project, you want to preserve your main conversation flow. You don't want it clogged with thousands of lines of debugging output or detailed file analysis. Subagents handle that complexity separately and return only the results you need. It keeps your workspace clean and focused.

**Specialized Focus** - Each subagent can have custom system prompts that give it expert-level knowledge in a specific domain. Your data analysis subagent can be instructed to always check statistical assumptions, handle missing data properly, and generate publication-quality plots. Your code review subagent knows to look for common bugs, security issues, and style violations. This specialized focus leads to higher quality results.

**Efficiency** - And here's where it gets really powerful: you can run multiple subagents in parallel. Need to analyze experimental data AND review code AND search literature all at once? Launch three subagents. They work simultaneously and report back when done. This parallel processing can dramatically speed up complex workflows.

For graduate students juggling multiple projects, this is transformative."

---

## Slide 9: Subagent Communication Diagram

**Explain the architecture:**
"This diagram shows how subagents fit into your workflow.

[Point to diagram elements]

At the center, you have the Primary Agent - this is your main Claude interface, your conversation partner.

Around it, we have several specialized subagents: code-reviewer, test-runner, data-analyzer.

Notice the arrows - they all point to and from the Primary Agent. **This is critical:** [read key point from slide] Subagents communicate only with the primary agent, not directly with users.

What does this mean in practice?
- You tell the Primary Agent what you need
- The Primary Agent delegates to appropriate subagent(s)
- Subagents do their work and report back to Primary
- Primary Agent synthesizes results and presents them to you

This architecture keeps your interaction clean and organized. You're not managing multiple conversations - you have one conversation, and the AI manages the delegation behind the scenes."

---

## Slide 10: Agent Workflow Diagram

**Walk through the flow:**
"This flowchart shows a typical workflow with subagents.

[Follow the flow on diagram]

It starts with you making a request. The Primary Agent analyzes whether this is a simple task it can handle directly, or a complex task that needs delegation.

For complex tasks, it launches specialized subagents - maybe multiple ones in parallel. Each subagent works independently with its own tools and context.

When subagents complete their work, they report results back to the Primary Agent. The Primary Agent synthesizes everything and presents you with a coherent answer or outcome.

Notice how this mirrors good project management in research - clear delegation, parallel work where possible, and centralized coordination."

---

## Slide 11: Data Collection Workflow Demo

**Transition to demo:**
"Let's see this in action with a data collection workflow demo.

[Prepare demo]

I'm going to show you a real scenario that many of you might face: collecting and processing data from multiple sources, running analysis, and generating a report.

Watch how the Primary Agent coordinates multiple subagents to handle different parts of this workflow simultaneously.

[Conduct demo - example workflow:]
- Show a complex data collection task
- Demonstrate subagent launching
- Show parallel execution
- Display final synthesized results

[After demo]
What you just saw would typically take you hours of manual work - downloading data, writing analysis scripts, debugging, generating plots. With subagents, this becomes a 10-minute supervised process where the AI does the heavy lifting and you guide the strategy."

---

## Slide 12: Creating Your Own Agents with Meta-Agent

**Introduce meta-programming concept:**
"Now here's where it gets really interesting - you can create your own custom subagents. And better yet, there's a meta-agent that helps you create other agents.

Let me explain the structure of a subagent configuration: [point to columns]

**Configuration Header** - This is YAML metadata that defines:
- The agent's name
- A description of when to use it
- Which tools it has access to
- Which AI model to use (Opus for complex reasoning, Sonnet for balanced performance, Haiku for speed)
- Even the color it displays in the interface

**Instructions Workflow** - This is where you define what the agent actually does:
- Start by fetching relevant documentation
- For new agent creation: analyze requirements, choose appropriate tools, write clear instructions
- For optimization: analyze current performance and improve

The meta-agent itself is defined this way. It's a subagent that creates and optimizes other subagents. Very meta, right?

What's powerful here is that you don't need to be an expert in prompt engineering. You can tell the meta-agent 'I need a subagent that validates my quantum chemistry calculations' and it will create one for you, complete with best practices pulled from current documentation."

---

## Slide 13: Tips for Creating Effective Agents

**Practical advice:**
"Based on experience with many custom subagents, here are four essential tips:

**1. Start with documentation fetch**
Always begin your agent instructions with fetching the latest documentation from Anthropic. Why? Because Claude Code is rapidly evolving - new features every week. You want your subagent using current best practices, not outdated approaches. This one step dramatically improves agent performance.

**2. Define a clear role**
One specific purpose, one clear responsibility. Don't create a Swiss Army knife agent that does everything. Make specialized agents. Not 'research-helper' but 'protein-structure-analyzer' or 'spectra-processor'. Narrow focus leads to better performance.

**3. Define clear input and output**
[emphasize] This is CRITICAL: Remember, subagents don't talk to users directly. They talk to the Primary Agent. So you must specify exactly what information they should return.

Bad: 'Analyze this data'
Good: 'Analyze this data and return a JSON file with statistical metrics plus a summary.txt with interpretation'

Pro tip: Having subagents write their results to files makes it easy for the Primary Agent to present findings to you.

**4. Use meta-agent to optimize**
Don't try to perfect your subagent on the first try. Create a basic version, test it, then ask meta-agent to optimize it. The meta-agent can identify inefficiencies, add better error handling, and improve clarity.

**Discussion question:**
What specialized subagents would help your research? Think about:
- Repetitive analysis tasks you do weekly
- Complex multi-step procedures you've documented
- Quality checks you perform on data or code

[Allow 2-3 responses and discuss how to scope them appropriately]"

---

## Slide 14: Claude Skills

**Introduce new concept:**
"Let's move to our third major topic: Claude Skills.

[Read slide] Skills provide specialized workflows and domain expertise.

Now you might be wondering - how is this different from MCP or subagents? Great question.

**Skills are pre-packaged workflows with instructions and best practices.** They're like having expert colleagues who can guide you through complex procedures.

For example:
- MCP gives Claude the ABILITY to edit PDF files
- A Skill gives Claude the KNOWLEDGE of best practices for extracting tables from scientific papers, handling images, maintaining formatting, etc.

**Skills provide domain-specific knowledge.** They might include scientific writing conventions, document processing workflows, or development best practices specific to certain fields.

**Skills run within your main conversation** - unlike subagents which have separate contexts. You invoke a skill, it guides the current conversation, then you continue.

Think of it this way:
- MCP = Tools in your toolbox
- Subagents = Specialized workers you can delegate to
- Skills = Expert knowledge and procedures you can reference

All three work together in a complete system."

---

## Slide 15: Skills Extend Claude - Examples

**Concrete examples:**
"Let's look at what skills enable in practice. Skills extend Claude with specialized knowledge - like having expert colleagues on call.

[Point to each column]

**Document Processing**
- PDF manipulation: extracting text and tables while preserving formatting, merging multiple PDFs, adding annotations
- Excel/spreadsheet analysis: complex formulas, pivot tables, data visualization, statistical analysis
- Word document editing: maintaining styles, cross-references, templates

For researchers, this means Claude can help you process all those supplementary files, extract data from PDFs, analyze spreadsheets from instruments.

**Content Creation**
- Scientific figures: publication-quality plots with proper labeling, color schemes appropriate for colorblind readers, vector graphics
- Scientific slides: LaTeX beamer presentations with consistent formatting, TikZ diagrams
- Poster design: layout optimization, visual hierarchy, poster template standards

Instead of spending hours tweaking matplotlib parameters or fighting with PowerPoint, describe what you want and the skill guides proper implementation.

**Research Workflows**
- Paper reading Q&A: systematic approach to literature review, extracting key methods and findings, identifying gaps
- Problem-solving cycle: structured approach to debugging, hypothesis testing, iterative refinement

These skills encapsulate best practices so you don't have to remember every detail."

---

## Slide 16: Skills vs MCP Tools

**Clarify the distinction:**
"Let me clarify the difference between Skills and MCP Tools, because this is a common question.

[Point to columns]

**Skills:**
- Workflow instructions - step-by-step procedures
- Domain expertise - 'this is how experts do it'
- Best practices guides - quality standards
- Multi-step procedures - orchestrating several actions

**When to use:** Complex workflows that require knowledge and judgment

**MCP Tools:**
- Function calls - discrete actions
- External system access - connecting to software/databases
- API integrations - programmatic interfaces
- Real-time data - fetching current information
- Action execution - actually doing things

**When to use:** External connections and specific actions

[Read key insight from slide]
**Skills guide HOW to work, MCP provides WHAT to work with**

Here's a concrete example:
- MCP tool: 'fetch_protein_structure(pdb_id)' - actually gets the data
- Skill: 'When analyzing protein structures, always check resolution, validate structure quality, consider missing residues, compare to homologs...' - guides the analysis

You need both. MCP gives capabilities, Skills ensure those capabilities are used expertly."

---

## Slide 17: Built-in Skills Examples

**Survey available resources:**
"Claude Code comes with several built-in skills, and there's a growing repository of community skills.

Let me highlight a few that are particularly useful for researchers:

**document-skills:pdf** - Comprehensive PDF operations: extracting text and tables, creating new PDFs, merging documents. Essential for processing literature and supplementary materials.

**document-skills:xlsx** - Spreadsheet expertise: formulas, data analysis, visualization. Your instruments export Excel files? This skill helps process them properly.

**mcp-builder** - A skill for creating MCP servers. It guides you through the process we discussed earlier. Very meta - it's a skill for building the tools that give Claude new capabilities.

**skill-creator** - Even more meta - a skill for building custom skills! You describe a workflow you want to capture, and this helps you create a proper skill definition.

**canvas-design** - Creating visual designs for posters and figures. Understands design principles, color theory, accessibility standards.

And many more at github.com/anthropics/skills. I encourage you to browse the repository - you'll find skills for web development, data science, creative writing, and increasingly, scientific domains.

The community is actively developing new skills, and I expect we'll see more domain-specific scientific skills emerging."

---

## Slide 18: Anatomy of a Skill

**Technical details:**
"If you want to create your own skill, let's look at how they're structured.

Skills are defined in a single file called SKILL.md, with two main parts:

**1. Metadata** - Simple YAML header:
- name: how to invoke the skill
- description: when and how to use it

**2. Instructions** - Markdown document containing:
- Purpose and overview: what this skill does
- Step-by-step procedures: detailed workflows
- When to use the skill: activation criteria
- References: links to tools, scripts, documentation, examples

That's it. It's just a markdown file with structure.

The beauty is that you can write these in natural language. You don't need special syntax or programming knowledge. Just document your workflow clearly.

**Pro tip:** Use the skill-creator skill to generate your SKILL.md files. Tell it what workflow you want to capture, and it will create a properly formatted skill definition for you. Then you can refine it based on your experience.

For researchers, this is perfect for capturing lab protocols, analysis procedures, or quality control workflows. Once captured as a skill, you and your lab members can invoke expert guidance any time."

---

## Slide 19: Skills Demo - Paper Reading

**Transition to demo:**
"Let me show you a practical skill in action: paper reading and analysis.

[Prepare demo]

This is a common task for all of you - you need to read papers, extract key information, understand methods, and integrate findings into your research.

Watch how the paper reading skill provides a structured approach.

[Conduct demo - example workflow:]
- Provide a PDF of a recent paper
- Invoke the paper reading skill
- Show how it guides systematic analysis
- Extract methods, results, and key findings
- Generate structured notes

[After demo]
Notice how the skill ensured we didn't miss important aspects? It prompted questions about methodology, statistical rigor, reproducibility. This systematic approach is what transforms casual reading into deep understanding.

You could create similar skills for your domain - protein structure analysis, spectroscopy interpretation, materials characterization."

---

## Slide 20: Hooks - App-Level Automation

**Introduce automation concept:**
"Now let's talk about Hooks - the automation layer that makes Claude Code behavior predictable and customizable.

[Read heading from slide] Hooks are user-defined commands that run automatically.

**What Are Hooks?**
- Shell commands that execute automatically
- Triggered by specific events in the Claude Code lifecycle
- Give you deterministic control over behavior

Think of hooks like triggers in a database, or lifecycle methods in programming. They let you inject custom behavior at specific points.

**Hook Events** - There are four main trigger points:
- PreToolUse: Runs BEFORE Claude executes any tool. Perfect for validation or safety checks.
- PostToolUse: Runs AFTER a tool completes. Good for logging or notifications.
- UserPromptSubmit: Triggers when you send a message. Can validate input or add context.
- Stop: Fires when Claude finishes a response. Useful for notifications or cleanup.

The key insight: Hooks make Claude Code behavior predictable and customizable. Instead of hoping Claude does something a certain way, you can enforce it with hooks.

For research environments where reproducibility and safety are critical, this is invaluable."

---

## Slide 21: My Essential Hooks

**Share practical examples:**
"Let me share three hooks I use constantly - these solve real problems I encountered:

**1. Safety Guard Hook - PreToolUse**
This blocks dangerous operations before they execute.

You might enable 'dangerously mode' to let Claude make broad file operations. But you don't want 'rm -rf /' to ever run! A PreToolUse hook can intercept commands, check against a blacklist, and block truly dangerous operations while allowing legitimate work.

I have mine check for:
- Recursive deletions in critical directories
- Force pushes to protected branches
- Operations on files outside the project directory

This gives you the productivity of fewer guardrails with the safety of human oversight.

**2. Task Completion Notifications - Stop**
When you're running long tasks - maybe Claude is processing 100 data files - you don't want to sit and watch. But you need to know when it's done or needs your input.

A Stop hook can:
- Play a sound when Claude finishes
- Send a desktop notification
- Log completion timestamps
- Even send you a message

Now you can start a task, switch to other work, and get alerted when attention is needed.

**3. Git Commit Standards - PreToolUse**
This enforces your team's conventions automatically.

Before any git commit executes, the hook checks:
- Branch naming follows conventions (feature/*, bugfix/*, etc.)
- Commit messages are concise (50-100 characters)
- No commits to protected branches

Instead of reviewing every commit Claude makes, the hook ensures standards automatically. This is especially valuable when you're working fast and might miss small issues.

[Pause]
What hooks would help your workflow? Think about:
- Safety checks for your domain
- Notifications for long-running processes
- Quality standards you want enforced"

---

## Slide 22: GitHub Integration Workflow

**Explain collaborative development:**
"Now let's talk about GitHub integration - because research increasingly happens in collaborative, version-controlled environments.

[Point to workflow diagram]

This diagram shows the recommended workflow when using Claude Code with GitHub:

1. Create feature branches for each task
2. Let Claude develop on those branches
3. Claude commits changes with clear messages
4. Claude pushes to remote and creates pull requests
5. You review the PR - this is your quality control gate
6. Once approved, merge to main

What's powerful here is the 'redo instead of edit' principle. If something isn't quite right in a PR, instead of manually fixing it, you can tell Claude to redo the task with additional requirements. This ensures:
- The AI learns from the feedback
- Everything goes through the same quality checks
- You have a complete history of the evolution

This might feel slower initially, but it leads to higher quality and better documentation."

---

## Slide 23: GitHub Integration Best Practices

**Key principles:**
"Three important principles for GitHub integration:

**1. Best practice: Redo tasks instead of editing when needed**
This comes directly from Anthropic's recommendations. When Claude produces something that's 80% right, resist the urge to manually fix the 20%. Instead, tell Claude what's wrong and have it redo the implementation.

Why? Because this ensures everything passes through your quality checks - hooks, tests, reviews. And it creates clean implementation from the start, not patches on patches.

**2. Everything is recorded and traceable**
Every decision, every change, every iteration is in your git history. This is invaluable for:
- Collaboration: teammates see why decisions were made
- Knowledge sharing: new lab members can understand project evolution
- Reproducibility: clear history of all changes
- Debugging: easy to identify when issues were introduced

For scientific research, this audit trail is crucial.

**3. GitHub CLI integration**
Claude Code handles all GitHub operations through the 'gh' CLI. You don't need to remember commands. Just prompt:
- 'Create a pull request for this feature'
- 'Check CI status on the PR'
- 'Merge the PR if tests pass'

Claude translates natural language to proper gh commands. One less thing to remember."

---

## Slide 24: Worktrees for Parallel Development

**Advanced technique:**
"Let me share an advanced technique that's incredibly useful: git worktrees.

**What are worktrees?**
Worktrees let you have multiple working directories for the same repository, each on a different branch. It's like having multiple checkouts of your repo, but they share the same git history.

**Perfect for parallel development:**
Imagine you're working on a complex analysis feature in one Claude Code session. Suddenly you discover a bug that needs immediate fixing.

Without worktrees, you'd need to:
- Stash your current work
- Switch branches
- Fix the bug
- Switch back
- Unstash

With worktrees:
- Open a new Claude Code session in a different worktree
- Fix the bug there
- Keep your original session running undisturbed

**Claude Code + Worktrees:**
This is especially powerful when you want to:
- Let agents work on different features simultaneously
- Test multiple approaches side-by-side
- Handle urgent fixes without disrupting current work
- Avoid conflicts between concurrent Claude Code sessions

For example, you could have:
- worktree-main: stable codebase for running tests
- worktree-feature-a: developing new analysis method
- worktree-feature-b: updating data processing pipeline
- worktree-hotfix: fixing urgent bug

Each has its own Claude Code session, working independently.

This is advanced, but once you try it, you won't want to go back to constant branch switching."

---

## Slide 25: Continuous Evolution

**Set expectations:**
"Before we wrap up, I want to emphasize something important about this ecosystem:

[Read bullets from slide]

**New features release almost every week** - Claude Code, MCP, skills - this is all rapidly evolving. What I showed you today will be more capable next month.

**Continuously update tools, workflows, and expertise** - Don't just learn once. Subscribe to the Anthropic blog, follow the GitHub repos, engage with the community. The best practices are still being discovered.

**Experiment with novel AI-driven methods** - This is cutting edge technology applied to research. You will find novel applications I haven't thought of. Your domain expertise combined with these tools will reveal new possibilities.

My encouragement: Start simple. Pick one aspect we covered today - maybe install one MCP server, or create one simple skill for a common task. Get comfortable with it. Then gradually expand.

The learning curve is real, but the productivity gains are substantial. And you're not alone - there's a growing community of researchers using these tools."

---

## Slide 26: Questions & Discussion

**Open the floor:**
"We've covered a lot today: MCP for connecting AI to tools, subagents for managing complexity, skills for capturing expertise, and GitHub integration for reproducible workflows.

Now I'd love to hear from you. Let's open this up for questions and discussion.

[Pause]

Some questions to get us started if needed:
- What part of your research workflow could benefit most from these tools?
- What concerns do you have about integrating AI into your research?
- What tools or systems in your lab would you want to connect via MCP?
- Has anyone already started experimenting with Claude Code or similar tools?

[Facilitate discussion]

---

**Closing:**
Remember, all the materials from this workshop will be available in the GitHub repository. I've included:
- These slides and speaking notes
- Demo code and examples
- Links to resources and documentation
- Sample MCP servers and skills to get you started

Feel free to reach out if you have questions as you start implementing these in your research. Good luck, and I'm excited to see what you build!

Thank you!"

---

## Additional Tips for Delivery

### Timing:
- Total workshop: ~90 minutes
- Introduction: 5 min
- MCP section: 20 min (including demo)
- Subagents section: 20 min (including demo)
- Skills section: 15 min (including demo)
- GitHub/Hooks section: 15 min
- Discussion: 15 min

### Engagement Strategies:
- Ask for show of hands at several points
- Include 2-3 discussion questions
- Encourage questions throughout
- Share specific examples from your own research

### Demo Preparation:
- Test all demos beforehand
- Have backup screenshots/videos in case of technical issues
- Keep demos short (3-5 minutes each)
- Prepare specific prompts in advance

### For Graduate Students:
- Emphasize time savings and productivity
- Connect to common pain points (literature review, data processing, repetitive analysis)
- Acknowledge learning curve but stress long-term benefits
- Highlight reproducibility and collaboration aspects

Good luck with your workshop!
