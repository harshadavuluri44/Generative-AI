'''

What is PYDANTIC?


Pydantic is a data validation library using Python type hints.

We define a schema as a class (subclassing BaseModel), and Pydantic:

    validates incoming/returning data against the declared types

    coerces/converts compatible types (e.g., "123" -> 123 for an int field)

    raises a clear ValidationError when data doesn't match the defined schema


----------------------------------------------------------------------------------------------------------------------------------------------------------------

Example:


from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(..., description="The role of the message sender")
    content: str = Field(..., description="The content of the message")


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(..., description="List of chat messages")


class ChatResponse(BaseModel):
    role: str = Field(..., description="The role of the message sender")
    content: str = Field(..., description="The content of the response")


description= is purely documentation (shows up in Swagger)


----------------------------------------------------------------------------------------------------------------------------------------------------------------

Where Pydantic classes are used in FastAPI:


1. @router.post("/chat", response_model=ChatResponse)

    Here the Pydantic class in the router -> validates the function's return value/output


2. async def generate_chat_response(request: ChatRequest):

    Here the Pydantic class in the function parameter -> validates the input against ChatRequest.
    This happens before the function body even runs.


'''
