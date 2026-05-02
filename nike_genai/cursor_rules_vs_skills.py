'''

Rule: 


Skill: A skill is like a detailed procedure - pull it out only when we need to perform that specific task.
    (Agent pulls out skill based on description of skill and user's prompt.)


------------------------------------------------------------------------------------------------


From the project: route-and-research-l3


Rule: question-completion.mdc is always injected into every converstaion.

    It says:
        Befor you(agent) do anything, make sure the user gave workspace URL, error text, and other identifiers.
        If anything is missing, ask. Don't proceed without them.


Rule: question-answering.mdc is always injected into every converstaion.

    It says:
        If an MCP tool fails, stop. Ask the user. Don't try to hack around it.




Skill: question-routing/SKILL.md

    This is a detailed procedure manual that AI reads only when it needs to answer a question. It contains:


    * A 6 step workflow (classify, query sources, filter, rank, answer, log telemetry)
    * A taxonomy table mapping keywords to platforms (Sole vs NGAP)
    * AWS account ID lookup tables
    * Which MCP tools to call and in what order
    * How to rank results by relevance
    * How to format the final answer with citations
    





'''