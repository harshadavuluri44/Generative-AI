'''

create a project : datahub_mcp

branch by default : production

by default db get's created: databricks_postgres (same name in all projects)


whatever the table we create it gets created in the databricks_postgres db unless we specify otherwise.



LAKEBASE_ENDPOINT is used to generate oauth token.

LAKEBASE_HOST and above token is setup connection to the lakebase 

----------------------------------------------------------------------------------------------------------------------------------------

What is Databricks Lakebase Endpoint?

    In Lakebase's hierarchy: Project -> Branch -> Endpoint

    When we create a Lakebase project, Lakebase auto-creates a production branch with a primary read-write endpoint.
    
    we can add more endpoints - e.g., a read-only endpoint for production data.

----------------------------------------------------------------------------------------------------------------------------------------

w.postgres.get_endpoint(name=endpoint_name)

    For example endpoint_name = f"projects/{LB_PROJECT}/branches/{LB_BRANCH}/endpoints/{LB_ENDPOINT}"

    here LB_ENDPOINT can be primary(default), read-only endpoint

    This function returns an object which contains host - needed for creation of connection to lakebase

example host: ep-lucky-forest-d16gs4rl.database.us-west-2.cloud.databricks.com


    This value changes based on PROJECT, BRANCH and ENDPOINT values

'''