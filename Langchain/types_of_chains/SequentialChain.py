'''

1. First chain -> generates company name.

2. Second chain -> Generate a catchphrase for that company


'''


from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain.llms import OpenAI


llm = OpenAI(temperature=0.9)

# First chain: company name

first_prompt = PromptTemplate(
            input_variables = ['product_name'],
            template = "What is a good name for a company that makes {product_name}?"
        )

chain_one = LLMChain(llm=llm, prompt=first_prompt)

# Second chain: catchphrase

second_prompt = PromptTemplate(
            input_variables = ['company_name'],
            template = 'write a catchy phrase for a company that makes {company_name}'
)

chain_two = LLMChain(llm=llm, prompt=second_prompt)

overall_chain = SimpleSequentialChain(chains=[chain_one, chain_two])


print(overall_chain.run("colorful_socks"))


# -----------------------------------------------------------------------------------------------------------------------------------------------------------


'''

If we prefer Databricks serving endpoint instead of OpenAI, we can use the following code:

Just replace line 13 with

from databricks_langchain import ChatDatabricks

line 16 with

llm = ChatDatabricks(endpoint='Harsha-serving-endpoint-1',
                    temperature=0.9)



NOTE - ChatDatabricks() only allows keyword arguments, not positional arguments. So endpoint key is mandatory.

'''
