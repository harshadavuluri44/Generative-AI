'''

.run() vs .invoke()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


.run() takes input as string only


.invoke() takes Dictionary/ Structured input




Use .run() when we just want a quick answer from an agent or chain.

Use .invoke() when we need structured inputs/outputs, metadata or want to integrate multiple components in a workflow.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



'''


response = agent.run("What is the square root of 256?")
print(response)  # "16"


response = agent.invoke({"input": "What is the square root of 256?"})
print(response)  # {"output": "16"}
