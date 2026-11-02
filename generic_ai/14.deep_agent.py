'''
What is a Deep Agent?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A Deep Agent is an agent built for long, complex, multi-step tasks, like research, coding or report writing. These tasks run for dozens or hundreds of tool calls.
Deep Agents is also the name of LangChain's open-source library for building them.



A Shallow Agent: a basic loop of LLM, tool call, answer. The works for simple tasks, such as "What's the weather?" or "Search for one asset". It breaks fown on
long tasks, because the context fills up, the agent loses track of the plan, and quality drops. 

Compass AI agent is currently a shallow agent (a basic loop with a max-iterations cap).



'''