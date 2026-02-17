'''

-- Find top 3 documents semantically similar to a query embedding


    SELECT id, text
    FROM vector_table
    ORDER BY cosine_similarity(embedding, [0.12, 0.98, ...]) DESC
    LIMIT 3;


the vector passed in ORDER BY class inside cosine_similarity is the query embedding/vector

embedding is a column in vector_table.



------------------------------------------------------------------------------------------------------------------------------------


COSINE SIMILARITY 

    is a measure of how similar two vector are, based on the angle between them.

    It doesn't care about magnitude(length) of vectors, only the direction.


    cosine similarity = A.B / |A||B|  (since it uses dot product, we can say closest vectors depends on angle between the 
    vectors)


    Always the value lies between -1<0<1

    In the above sql query, top 3 vectors are retrieved such that whose cosine similarity with vector B(query vector) is 
    almost near to 1.

------------------------------------------------------------------------------------------------------------------------------------



USE ai_similarity function in databricks for the above usecase.

NOTE - cosine_similarity is not available in databricks sql.


------------------------------------------------------------------------------------------------------------

FAISS-CPU

    FAISS (Facebook AI Similarity Search) is a library for fast similarity search in large collection of vectors.

    FAISS runs on CPU, no GPU's required.



'''