'''


Input tokens  ->   LLM     ->  Output tokens


Input tokens can include:
    System Prompt
    Tool/MCP definitions
    Conversation history
    User Query


Output Tokens = What the LLM generates

--------------------------------------------------------------------------------------------------------------------------------------------------

Prompt Caching


If a large part of your input is repeatedly the same, the model/provider can cache the processing of that repeated prefix.


Example:
    System Prompt:      10,000 tokens   -> same
    User Query:         100  tokens     -> changes


Instead of fully processing the 10,000 token system prompt every time, the cached processing can be reused.

--------------------------------------------------------------------------------------------------------------------------------------------------


Cache Write


The first time a cacheable prompt prefix is processed:

    10,000 system tokens  ->  CACHE WRITE

The system creates/stores reusable cached model state.

--------------------------------------------------------------------------------------------------------------------------------------------------

CACHE READ


On a later request with the same cacheable prefix:

    10,000 system tokens -> CACHE READ


The request still contains same system prompt, but their previously computed system prompt tokens are reused and instead of recomputation.

--------------------------------------------------------------------------------------------------------------------------------------------------



Cost for CACHE READ < recomputing of system prompt tokens.


'''