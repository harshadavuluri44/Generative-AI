# Example: Simple LLMChain

    # Image we want to generate a company name for a product.

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
            input_variables = ['product_name'],
            template = "What is a good name for a company that makes {product_name}?"
        )

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("colorful socks"))


'''

Output: “Rainbow Socks Co.”

Here:

    Input = "colorful socks"
    Prompt formats it: "What is a good name for a company that makes colorful socks?"
    LLM generates the answer.
    Chain returns the final result.

'''