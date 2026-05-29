'''

Push vs Pull between SOURCES and DataHub Metadata platform


PUSH

Definition: The source systems (Airflow, dbt, etc.) actively sends metadata to DataHub.
Mechanism: Usually via plugins, APIs etc.
Example: Airflow pushes DAG rub metadata (task status, scheduling info) into DataHub.


PULL

Defintion: DataHub fetches metadata from source systems by connecting to it.
Mechanism: Ingestion jobs, crawlers that query source systems.
Example: DataHub periodically pulls DAG definitions from Airflow.


------------------------------------------------------------------------------------------------------------------------


Why push or pull matters?


Push is better for event-driven, real-time lineage and monitoring.
Pull is better for scheduled, batch ingestion.



------------------------------------------------------------------------------------------------------------------------


Push -> Source system says: "Here's what I just did."
Pull -> DataHub asks: "Tell me what you did."


------------------------------------------------------------------------------------------------------------------------



NOTE: Whenever metadata updates happens in DataHub platform we can notify in slack etc, using REST/GraphQL API's or stream integrations.


GraphQL is not SQL, but it is a query language for APIs. You send queries in the request body, and server responds with JSON shaped exactly like query.


'''