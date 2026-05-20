'''

WHAT are CHAINS in LangChain?

--------------------------------------------------------------------------------------------------------

Chains are one of the core concepts in LangChain.


Chains in LangChain are WORKFLOWS that combine multiple components (like prompts, language models and output parsers) together in sequence, so that the output
of one step becomes the input of the next. They let us build structured pipelines instead of making isloated calls to a language model.



sequential processing workflow:  input -> step 1 -> step 2 -> ... -> output


    Each step can be:

        A PromptTemplate (formats user input into structured query)

        An LLM call (send the prompt to language model)

        A parser (extracts or formats the model's response).













'''

