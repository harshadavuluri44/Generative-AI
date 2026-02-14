'''

RAG combines an LLM with an external knowledge source (like documents, database, PDFs).


RAG is a technique where relevant external data is retrieved at query time based on user question and provided to LLM to generate a
response


Before generating an answer, it retrieves relevant information and feeds it to the LLM, making responses more accurate, up-to-date,
and grounded.



In Short:

    LLM = Brain (language understanding & generation)
    RAG = Brain + Open-book (retrieves real data before answering)


--------------------------------------------------------------------------------------------------------------------------------------

Fine-tuning is not the better option when the specific data get's updated frequently

    Then here come's RAG.

-------------------------------------------------------------------------------------------------------------------------------------

PERPLEXITY is completely developed based on RAG applications.

-------------------------------------------------------------------------------------------------------------------------------------




Data (pdf, html, etc) ->    parsing (chunks)   ->   Embeddings (text to vectors)    -> VECTOR DB


User    ->    Query     -- Embeddings -->  VECTOR DB  -- Context + prompt --> LLM       -> Output



Here prompt is handeled in RAG pipeline, please find an example below.

Ex: You are a helpful assistant. Use the following context to answer the user's question.

    Context:
            [retrieved chunk 1]
            [retrieved chunk 2]
            [retrieved chunk 3]

    Question: What are the key points in the HR policy document?



-------------------------------------------------------------------------------------------------------------------------------------

Example in Databricks


User Query to -> RAG pipeline -> vector DB -> prompt -> triggers LLM (serving endpoint) -> response.

-------------------------------------------------------------------------------------------------------------------------------------

NOTE:
In a basic RAG pipeline, the whole chunking -> embeddings -> vector DB search still happens, even if unnecessary. 
But in smarter pipelines, we can add a ROUTING step to skip retrieval when the query doesn't need external data.

'''