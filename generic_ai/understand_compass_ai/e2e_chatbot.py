'''

When the user hits a query in Compass AI chatbot, then below API is called


/mcp/query/stream


This api recieves user query and returns the response as a Server-Sent Events stream.


The function inside this api is query_mcp_agent_stream()

This takes request as input paramter, (request input follows MCPQueryRequest Pydantic model schema)

    Example input from frontent team, when this api is callled


    {
                "query": "What assets are available?",
                "session_id": "5b0a2d2c-3e6c-4f87-9a87-9f8e1c4f2b80",
                "user_email": "anirban.paul@nike.com",
                "user_name": "Anirban Paul",
            }


And also this function actually dives into logic, it has dependency injection - function get_mcp_service is called(which returns MCPService class object/instance)
as an input parameter to this function 


Now before understanding the logic of query_mcp_agent_stream(), let's understand the logic of get_mcp_service().

    Now instance MCPService class has below attributes

        mcp_server_url,
        endpoint name,
        _shared_llm, _cached_tools, _cached_prompts, _cached_system_prompt, _cached_bound_llm



'''