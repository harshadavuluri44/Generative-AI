'''

CREATE EXTENSION IF NOT EXISTS vector; really does

This SQL command is executed inside a PostgreSQL database (in your case, Lakebase, which is Databricks Postgres OLTP service).
It enables the pgvector extension in that database.

pgvector is not a table, not a catalog entry, and not a Databricks-wide toggle. It's a Postgres feature that adds a new data type (vector) and operators for 
similarity search.





'''