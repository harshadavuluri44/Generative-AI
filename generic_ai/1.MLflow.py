'''

MLflow is an open-source platform for the lifecycle of ML and GenAI applications. MLflow is created and developed by Databricks.

--------------------------------------------------------------------------------------------------------------------------------------------------




mlflow.set_tracking.uri("datbricks")    -   Tells MLflow where to send data: Databricks workspace.

mlflow.set_experiment("/Shared/compass-ai-dev")     -   Chooses which experiment the traces go into. it must be a workspace path, and it's created if it doesn't exist.
        we should pass workspace folder path.

mlflow.langchain.autolog()  -   Turns on automatic tracing of LangChain calls.



mlflow_traces_enabled = True,   -   Not an MLflow setting   -   This is custome flag in compass ai project.

--------------------------------------------------------------------------------------------------------------------------------------------------

uri in mlflow.set_tracking.uri() => Uniform Resource Identifier

The values can be
                    "databricks"
                    "http://localhost:5000"     -   Local MLflow server
                    "https://mlflow.mycompany.com"  -   A self-hosted remote MLflow server
                    "postgresql://user:pw@host/db"  -   A PostgreSQL database directly.

--------------------------------------------------------------------------------------------------------------------------------------------------



'''