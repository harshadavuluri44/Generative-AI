'''
Singleton Service



A singleton is a design pattern where we guarantee that only one instance of a particular object exists for the lifetime of program,
and everyone who asks for it gets that same shared instance rather than a fresh one each time.


@lru_cache() (from Python's functools module) memoizes the function's return value.
-----------------------------------------------------------------------------------------------------


Why singleton make sense in MCPService?

Constructing MCPService is expensive - Cerberus vault calls, OAuth negotiation, buidling an LLM client.
If it were re-created on every request(as would happen with plain Depends(get_mcp_service) and no @lru_cache), every single API call would pay that setup cost again, which would be slow and wasteful


Instead: pay the setup cost once (on the first request), then reuse the same object.

-----------------------------------------------------------------------------------------------------

EXAMPLE SCENARIO:


10:00 AM IST - user_1's query request in chatbot

1. FastAPI receives POST /mcp/query/stream with query_1
2. FastAPI sees service: MCPService = Depends(get_mcp_service) and calls get_mcp_service()
3. This call doesn't go straight to function body - it first goes through the wrapper @lru_cache() installed around it. The wrapper checks its internal cache dict: empty (first call ever since the process started) -> cache miss.
4. since no cache available, the wrapper calls the actual get_mcp_service function boday - logic runs - return MCPService instance, call it svc_A.
5. The wrapper stores svc_A in its cache dict.
6. The wrapper returns svc_A. FastAPI binds it to service and runs query_mcp_agent_stream(request=query_1, service=svc_A)




10:02 AM IST - user_2's query request in chatbot

1. FastAPI receives POST /mcp/query/stream with query_2
2. Same as before: FastAPI calls get_mcp_service() again - this is a fresh, independent call.
3. It goes through same @lru_cache() wrapper. The wrapper checks its cache dict: this time it finds an entry -> cache hit.
4. The wrapper returns svc_A immediately, without executing any of the construction logic code at all.
5. FastAPI binds service = svc_A (the exact same object user_1 got) and runs query_mcp_agent_stream(request=query_2, service=svc_A)



So: two separate HTTP requests, two separate calls to get_mcp_service(), but only one real MCPService object (svc_A) is ever constructed - both users requests share it.







'''