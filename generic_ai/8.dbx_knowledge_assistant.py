'''
The w.knowledge_assistants SDK namespace exists, but it's only for lifcycle/managemet operations - list_knowledge_assistants(),
list_knowledge_sources(), create/update/delete config.


There is no w.knowledge_assistants.ask(...) or .chat(...) inference method - because a Knowledge Assistant isn't a Python object living in your notebook's process.
It's a deployed model artifact running in its own serving container, elsewhere in the Databricks control plane. The only way to talk to any
running model/agent in Databricks - Knowledge Assistant, Supervisor Agent, Custom Agent, or a plain LLM - is over the network, to its serving endpoint.


'''