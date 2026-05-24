'''

WHAT are CHAINS in LangChain?

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Chains are one of the core concepts in LangChain.


Chains in LangChain are WORKFLOWS that combine multiple components (like prompts, language models and output parsers) together in sequence, so that the output
of one step in workflow becomes the input of the next step in workflow. 

They let us build structured pipelines instead of making isloated calls to a language model.



sequential processing workflow:  input -> step 1 -> step 2 -> ... -> output


    Each step can be:

        A PromptTemplate (formats user input into structured query)

        An LLM call (send the prompt to language model)

        A parser (extracts or formats the model's response).



----------------------------------------------------------------------------------------------------------------------------------------------------------------


1. LLMChain: Simplest chain. Takes a prompt template + input, sends it to the LLM, and returns the response.



2. SequentialChain: Connects multiple chains in order. The output of one chain becomes the input of the next.



3. RouterChain: Routes input to different chains based on conditions.


'''