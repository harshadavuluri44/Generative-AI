'''

LangChain is an open-source library and framework designed to simplify the development of applications built on top of
large language models (LLMS).

LangChain provides 
* LLM Interfaces -> Unified wrappers for models like OpenAI, Anthropic, Ollama, etc. to work with them (see below python code)
* Integrations -> connectors to external tools, APIs, and databases.
* RAG -> embedding + vector database support to ground LLMs in custom knowledge



'''

# we can import different models from langchain_openai, langchain_ollama, langchain_community etc.

from langchain_community.llms import Ollama

llm = Ollama(model="llama2")
response = llm.invoke("pick a number between 1 and 50")
print(response)
