'''
Agent Memory & Context Engineering
----------------------------------------------------------------------------------------------------------------------------------------------------------------

1. The foundation: LLMs are stateless

        - An LLM has no memory of its own. Each API call starts from zero.
        - It only knows what you send in that single call. This is its context.
        - Chat apps seem to remember because the app re-sends the earlier messages every time.
        - Common misconception: "the agent has memory". It doesn't. We build and manage memory around the model.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Basic terms

        - Context: All the text the model sees on one call.
        - Context window: Maximum number of tokens the model can accept per call (e.g 128k or 200k.)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. What's inside the context

        - System prompt
        - Tool definitions
        - User message
        - AI message
        - Tool result
        - AI message
        - User message 2  (newest question)

    Everything above is re-sent on every turn of the loop.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4. Why context needs to be managed/engineered?????

        The longer an agent runs, the more the context fills with tool results, etc....

    Then these 3 failure modes:

        - Bloated: too much noise, so the model gets distracted and accuracy drops.
        - Stale: old, outdated info misleads the model.
        - Missing: the needed fact was never given to the model.


    Other side effects of a big context:

        - Cost goes up, because we pay per token.
        - Latency goes up, because bigger prompts are slower.
        - Hard limit: exceeding the window causes errors or forced truncation.

    IMPORTANT: every message is re-sent every turn. A 50K-token tool result in turn 1 is paid for again in truns 2,3,4 and so on. The cost compounds.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

5. Definitions

    CONTEXT ENGINEERING: Deciding what goes into the context window at each step of an agent's run. Context engineering manages everything the model sees across
    a long loop.

    AGENT MEMORY: How an agent keeps and reuses information beyond what fits in the window. It is built by us, not provided by the model.


    TWO TYPES OF MEMORY


                    SHORT-TERM                                                  LONG-TERM

        One conversation or run                                             Across conversations
        Inside the context (the message list in point 3)                    Outside, in a file or database
        Gone when the run ends                                              Persists
        Hard Limit: 128k tokens                                             Practically unlimited

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

6. The core principle

        Move context out of the active window without deleting it. Keep the window small and relevant, and keep everything else retrievable.


        For example: The tool result is at <file_path>, use it if needed.
                            write a tool(which helps LLM to read file if needed.)

    So memory is not magic inside the agent. Our code stores it. The model only reads when it is shown, or fetches through tools when it is given and needed.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------



KEY TAKEAWAYS:


1. The LLM is stateless, and context is everything it sees.
2. "Agent Memory" is something we build. It is not built into the model.
3. Storage is chosen by us. The harness automates storing and pointing to it. The model chooses when to read it back.


'''