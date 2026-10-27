'''
Async / Await:


1. The core problem: waiting

Most of the time a request spends is waiting, not computing. It waits for a database, an LLM, an embedding API, an MCP tool. During that time the CPU is idle.


Async is a way to use that idle time to server someone else.


Code trigger's database, LLM > (50-100ms) database, LLM gives responses.

The time between above 2 is called latency, this is where async and await comes into play, and calls other users request.

------------------------------------------------------------------------------------------------

2. FOundation Concepts


* One worker does on thing a time.
    - A worker is a thread (or a CPU core). It can execute only one line of Python at any instant.
    - If the worker is stuck waiting (blocking), nothing else runs on that worker.


* Blocking vs non-blocking wait

    - Blocking                  The worker sits idle and stuck until the result arrives from database/llm etc
    - Non-blocking (async)      The worker steps away, does other work, and comes back when the result is ready.


* 3 ways to server many users

    Sequential, one thread, blocking        A finishes completely, then B starts.           slow for everyone.

    Many threads (sync) - many workers      One thread per request.                         Each thread costs memory. It doesn't scale to thousands of users.

    Async, event loop                       One thread, and tasks switch at every await.    Very cheap, it scales well when the work is mostly waiting.

------------------------------------------------------------------------------------------------

3. The restaurant analogy


    waiter = event loop (one thread)
    Tables = user requests
    Kitchen = DB / LLM
    Blocking waiter = takes and order and stands in the kitchen until the food is ready. Even other table waits.
    Async waiter = hands in the order, serves other tables, and returns when the food is ready.


------------------------------------------------------------------------------------------------

4. The keywords


    async def f():                      Defines a coroutine: a function that is allowed to pause.
    await x                             Makes f can't continue until x is ready. pause f and let loop run other things and wake me when x is done.
    asyncio.to_thread(f, ..)
    asyncio.gather(a,b)


    RULES

    - await only works inside async def.


------------------------------------------------------------------------------------------------

5. The big misconception

Wrong: While await runs, the next lines in the same function run.


Right:
    
    Inside one function, code still runs top to bottom in order.
    The line after await always wait for the result, and gets it.
    What runs during the wait is other tasks: other user's request or other coroutines.


    vec = await embed(query)    # This function pauses here
    if vec:                     # This line runs only after the await is done.
        .....


------------------------------------------------------------------------------------------------


7. Timelines
    One thread, blocking:


    A: [embed..wait..][db..wait..][done]
    B:                                  [embed..wait..][db..wait..][done]
    Async (single thread):


    A: [embed] ..waiting..  [db] ..waiting.. [done]
    B:         [embed] ..waiting.. [db] ..waiting.. [done]
    Within A the order is the same (embed, then db, then done). B just doesn't have to wait for A to finish.

    Important: async does not make one request faster. It lets many requests overlap. To make one request faster, use gather.


------------------------------------------------------------------------------------------------



SUMMARY:


A worker(thread) can run only one piece of Python at a time. Most request time is spent waiting on a database, an LLM or the network. A blocking wait freezes that woker, and with one worker everyone queues behind it.
await marks a spot where this function must wait, so the event loop steps away and runs other tasks until the result is ready. Inside a function, order stays top to bottom, and the next line always receives the real result.
Async improves throughput (many users at once). gather improves the latency of one request. Blocking libraries must go through asyncio.to_thread so they don't freeze the single event-loop thread.


------------------------------------------------------------------------------------------------



1. If function A is async, when we call function A beside await -> await A()

2. If function A is not async, when we call function A beside await -> await asyncio.to_thread(A, params)



'''