from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('path to pdf file')

doc = loader.load()

# -----------------------------------------------------------

from langchain_text_splitters import RecursiveCharacterTextSplitter

rcts = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

doc = rcts.split_documents(doc)

# -----------------------------------------------------------

from databricks.vector_search.client import VectorSearchClient

vsc = VectorSearchClient()


vsc.create_endpoint(endpoint_name='rag_endpoint', endpoint_type='STANDARD')


endpoint_config = vsc.get_endpoint(endpoint_name='rag_endpoint')

# -----------------------------------------------------------


vsc.create_delta_sync_index_and_wait(
    endpoint_name='rag_endpoint',
    index_name='development.team_data_technology_foundation.harsha_rag_index',
    source_table_name='development.team_data_technology_foundation.harsha_rag_table',
    pipeline_type='TRIGGERED',
    embedding_source_column='content',
    primary_key='chunk_id',
    embedding_model_endpoint_name= 'databricks-bge-large-en',
    verbose=True

)

# -----------------------------------------------------------

endpoint_url = "https://nike-sole-react.cloud.databricks.com/serving-endpoints/Harsha-serving-endpoint/invocations"