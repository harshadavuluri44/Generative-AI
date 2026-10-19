'''
FACTORY FUNCTION



A factory function is a function whose entire purpose is to construct and return an object of a class, instead of us constructing the object ourselves.


Why use a factory function, instead of just calling MCPService(token_provider=..., endpoint=....) directly wherever we need it?


Because constructing the object correctly here is complicated - it requires several steps done in the right order:

    - fetch config
    - pull secrets out of a vault (cerberus here)
    - build a TokenProvider from the above


HERE get_mcp_service() is the factory - it encapsulates all that setup logic in one place and hands back a ready-to-use MCPService object.

Anyone who wants an MCPService object/class just calls the get_mcp_service() factory, as they don't need to know or repeat any of the construction prerequisites.



'''