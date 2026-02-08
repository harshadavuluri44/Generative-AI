'''

LLM's are trained with huge data in the past,

    So it cannot answer who won cricket match IND vs USA yesterday?
       it cannot connect to NIKE's database or etc, to answer regarding the NIKE's DTF project or etc.


HERE COME's UP AI AGENT


                                       ->(Request)
    
    User prompt     ->      LLM      --- TOOL CALL --->             TAVILY (3rd party API / wrapper)
                                     
                                       <-(Response)


                                       
A TOOL CALL happens when LLM realizes it cannot answer a user's query on its own (e.g., the question requires fresh data or specialized computation).


Here AI AGENT is the one which completes TOOL CALL (i.e sending prompt from LLM to TAVILY and sending back respective answer.)

----------------------------------------------------------------------------------------------------------------------------------------------

AGENTIC AI = AI Systems (single or multiple agents) that autonomously plan, reason, use tools, and collaborate to achieve goals.


SCENARIO: Create a blog from youtube video and publish it on a website.


AGENTIC AI Blueprint for the above Scenario


1. Video Retrievl Agent
    * Role: Fetch the video content from YouTube (via API or link).
    * Tasks:
            - Extract metadata (title, description, tags).
            - Download or transcribe audio into text.

2. Transcription Agent
    * Role: Convert video speech into text.
    * Tasks: 
            - Use speech-to-text MODELS (e.g., Whisper).
            - Clean up filler words, pauses, and errors.
    * Output: Raw transcript of the video

3. Summarization Agent
    * Role: Transform transcript into structured notes:
    * Tasks:
            - Identify key themes, arguments, and examples.
            - Break down into sections (intro, body, conclusion).

4. Blog Writing Agent
    * Role: Convert notes into a polished blog post.
    * Tasks:
            - Rewrite in blog style (engaging, SEO-friendly).
            - Add headings, subheadings, and call-to-action
    * Output: Draft blog article

5. Editing & Quality Agent
    * Role: Review and refine blog draft
    * Tasks:
            - Check grammer, tone, readability.
            - Ensure orginality (avoid plagiarism).
            - Optimize for keywords.

6. Publishing Agent
    * Role: Uploade blog to the target website.
    * Tasks:
            - Format content for CMS(WordPress, Medium, etc.).
            - Add images, metadata and SEO tags.
            - Schedule or publish post.


Collabration of above 6 Agents to complete the task is AGENTIC AI

-------------

Key TakeAways.

1. Instead of 6 agents, single agent could perfrom all tasks.
   But in practice, breaking tasks into multiple specialized agents has advantages: 
        * Modularity (Easier to debug and improve one step without breaking the whole system.)
        * Scalability(you can swap Agent 2 with better agent)

2. We can think each agents as a piece of code (often wrapping an LLM + tools) inside a pipeline.
    Workflow pipeline : A1 -> A2-> A3 -> A4

    But unlike a rigid pipeline, agents can be dynamic

3. In each agent, use LLM wherever required.

'''


# TAVILY is a company that builds infrastructure to connect AI agents to the web.
        # Its main product is a search and retrieval API designed specifically for LLMs and RAG.


# WHISPER is an automatic speech recognition (ASR) model developed by OpenAI. - Convert spoken audio into text (speech-to-text)
# How it differs from LLMs - It os trained on audio + text.