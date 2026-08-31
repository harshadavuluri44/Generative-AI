'''

What is p95 latency?


p95 latency = 95th percentie latency of all requests.


Suppose a vector database receives 1,000 search queries.

we measure how long each query takes and sort them from fastest -> slowest.



95th percentile of 1,000 = 950th query.


So, if 950th query takes 40ms, then:   p95 latency = 40ms



That means 95% of requests finish in 40ms or less, while the slowest 5% take longer.
--------------------------------------------------------------------------------------------------------------------------------------------


Note: we can import a class in mcp_agent.py to mcp_service.py file.

Importing doesn't create a new instance/object of class.


from services.mcp_agent import MCPAgent as _MCPAgent


# we need to create a new instance and then use the attributes/methods of it.

agent = _MCPAgent()
--------------------------------------------------------------------------------------------------------------------------------------------


Field() is a Pydantic function used to add extra metadata/validation rules to a variable, beyond juts its type annotation(ex: str).

It lets us specify things like:

    - default value
    - documentation metadata (description, etc.)

Without Field(), we'd just write query:str, but then we have no way to attach description, etc.

Example:  query: str = Field(..., description="User query to process with MCP agent")

if default value is ...(Ellipsis), this field has no default - it is mandatory.

if it is not mandatory - we can write default=None.



session_id: Optional[str] = Field()


here Optional[str] means session_id should be a string or None(optional).
'''