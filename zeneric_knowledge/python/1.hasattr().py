'''
In Python, variables/properties and methods/functions inside an object or class are called as attributes, not only variables.
------------------------------------------------------------------------------------------------

hasattr()

    is a built-in function that checks if an object has a given attribute or not.


Example

    from fastmcp import FastMCP

    mcp = FastMCP("test server")


    if hasattr(mcp, "streamable_http_app"):

        # Do this

The reason to use hasattr() is a defensive compatibility check - streamable_http_app was added in a newer version of fastmcp library.
This pattern guards againts running on an older version that doesn't have that method.







'''