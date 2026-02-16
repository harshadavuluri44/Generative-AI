'''

TIP of the Day: Retrieval Quality Matters More Than Model Size

* Many poeple focus on the LLM (GPT, Gemini, etc.), but in RAG the retrieval step is the real backbone.

* If vector DB returns irrelevant or noisy chunks, the LLM will produce weak or hallucinated answers - even if it's a powerful model.

* To improve retrieval quality:
    * chunk smartly: Instead of arbitary splits (e.g., every 500 tokens), split by semantic boundaries (paragraphs, sections, headings).
    * Experiment with top-k: Sometimes retrieving fewer but highly relevant chunks (top-3) works better than flooding the LLM with 10.

In short: Better retrieval = better answers. Even a smaller LLM can shine if fed the right context.

'''