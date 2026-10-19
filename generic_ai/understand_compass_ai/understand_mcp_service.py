f'''

MCPService class constructor has below values


    mcp_server_url (coming from npe component yaml, as mcp_service.py code lies in marketplace-api)
    serving endpoint

    _shared_llm, _cached_tools, _cached_prompts, 
    _cached_bound_llm


    _get_shared_llm():

            What it does?


        prepares _shared_llm

        This function doesn't start, deploy or call the Databricks Serving endpoint. 

        It only build's a variable _shared_llm which holds TokenAwareChatDatabricks() class object. [No .invoke is done here]

        _shared_llm variable is used once after, bind_tools() is done and in the mcp_agent.py


    _build_agent(llm):

        This function returns MCPAgent class instance.

        MCPAgent constructor has MCP client class instance.

    
    _ensure_cache():

            What it does?

        prepares _cached_tools, _cached_prompts by connecting to mcp server

        and then _cached_bound_llm.

    
        llm = _get_shared_llm() [i.e _shared_llm]

        With the help of MCPAgent instance from _build_agent(),  connects to MCP client to list tools, system_prompt.

        So here _cached_tools, _cached_prompts, _cached_bound_llm are prepared.


    _query_stream():

        calls the run_stream() method of MCPAgent class instance to get response chunk by chunk.



'''