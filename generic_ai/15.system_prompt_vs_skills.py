'''
A system prompt and a skill are both instructions for an LLM. They DIFFER in WHEN they're LOADED and HOW MUCH of the MODEL'S CONTEXT they use.


SYSTEM PROMPT:

    The system prompt is the always-on baseline instruction set. It's sent with every request.

        - It defines the model's role, rules, and available tools.
        - It is always in context, so every token costs you on every turn.
        - It should be short and general: "who you are and how you behave."
        
    Example: "You are Compass AI, a metadata discovery assistant. Never invent credentials. Use the tools provided."


SKILL:

    A skill is a packaged, task-specific playbook that is loaded only when needed.

        - It's usually a folder with a SKILL.md file, plus optional scripts and reference docs.
        - Only a short description of each skill (a line or two) sits in the system prompt. The model reads the full SKILL.md when a task matches.
        - It holds detailed, procedural knowledge: step-by-step workflows, commands, gotchas, and templates.

    Example: the nim-mcp-deploy skill contains the exact databricks sync and databricks apps deploy steps. Those steps are irrelevant to most conversations, so they aren't loaded until you ask about deploying MCP.



KEY DIFFERENCES:

                    SYSTEM PROMPT                   SKILL

    Loaded          Always                          On Demand
    Scope           General behavior                One specific task or domain
    Size            Small                           Can be large
    Context cost    Paid on every trun              Paid only when used
    Content         Identity, rules, constraints    Procedures, commands, examples

------------------------------------------------------------------------------------------------------------------------------------------------


Use System prompt for things that must apply to every interaction, like safety rules, and project-wide conventions.

Use skill for a repeatable workflow that only matters sometimes, like deployments, log traige, or ETL creation.

------------------------------------------------------------------------------------------------------------------------------------------------


If we put everything in the system prompt, it gets bloated, it costs more, and the model's attention gets diluted.

And if we put a global rule in a skill, the model may never load it.

    



'''