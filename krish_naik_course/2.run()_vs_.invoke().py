'''

.run() vs .invoke()
---------------------------------------------------------------------------------------------------------------------------------------------------------------

- .run()    -> takes input as a string only.
- .invoke() -> takes a dictionary / structured input.

- Use .run()    when we just want a quick answer from an agent or chain.
- Use .invoke() when we need structured inputs/outputs, metadata, or want to integrate
                multiple components in a workflow.

NOTE: .run() belongs to older LangChain versions and is now deprecated — use .invoke() instead.


---------------------------------------------------------------------------------------------------------------------------------------------------------------

agent.invoke() vs model.invoke()


- model.invoke() accepts a string, a PromptValue, or a list of messages.
- agent.invoke() expects a structured dict input (e.g. {"input": "..."}).

- AGENT = orchestration layer -> wants structured inputs.
- MODEL = raw LLM / chat model -> wants prompt-like inputs.

'''


response = agent.run("What is the square root of 256?")
print(response)  # "16"


response = agent.invoke({"input": "What is the square root of 256?"})
print(response)  # {"output": "16"}


response = model.invoke("what is square root of 256?")
