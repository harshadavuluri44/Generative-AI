'''

Message types


1. System message - Tells the model how to behave and provide context for interactions.

2. Human message  - Represents user input and interactions with the model.

3. AI message     - Output by the model, including text content, tools the model wants to run, and metadata.

4. Tool message   - Represents the outputs of tool calls.



Example:


messages = [

    SystemMessage("You are helpful assistant for Nike metadata or data catalog".)
    HumanMessage("How many products are there in the catalog?")
    AIMessage("There are 1000 products in the catalog.")
    ToolMessage(tool_calls=[
        {
            "name": "get_product_count",
            "args": {"product_id": "123"}
        }
    ])
]


NOTE: AIMessage has model's reply, tools the model wants to run, but not the tool results.

It also carry usage_metadata()


response.usage_metadata looks like

{
    'input_tokens': 8,
    "output_tokens": 304,
    "total_tokens": 312,
    "input_token_details": {"cache_read": 0, "cache_creation": 0}
}


'''