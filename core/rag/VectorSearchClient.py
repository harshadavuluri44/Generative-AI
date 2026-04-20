'''

VectorSearchClient in Databricks.


from databricks.vector_search.client import VectorSearchClient



VectorSearchClient class helps to

            create vector search endpoint for similarity search

            create vector search index table from source table.


------------------------------------------------------------------------------------------------------------------------------------


VECTOR SEARCH INDEX

    A vector search index is a special data structure that organizes embeddings so they can be searched efficiently.

        Without an index, finding similar vectors would require comparing query against EVERY single embedding in table (very slow).
        The index uses algorithms like HNSW or IVF to make similarity search fast.


vsc = VectorSearchClient()

index = vsc.create_delta_sync_index_and_wait(
                endpoint_name,
                index_name,
                source_table_name,
                pipeline_type,
                primary_key,
                embedding_dimension,
                embedding_vector_column_name,
                embedding_model_endpoint_name,
                verbose=True)


create_delta_sync_index_and_wait() reads delta table that contains resume chunks and embeddings, builds an optimized search index
and waits for the index to be ready.


'''