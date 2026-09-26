'''

1. what is -q in pip install?

pip install -q "databricks-sdk>=0.118.0" "pyscopg[binary]>=3.1.18"

    -q means quiet -- it suppresses most of the install output (progress bars, "already satisfied" lines) so our cell output stays clean
    -qq means even quieter -- it suppressess even more output
    -qqq means slient.

--------------------------------------------------------------------------------------------------------------

2. What is Any from typing?

from typing import Any

Any is a type hint that means "parameter/variable can be of any type"


Example:   def fun(x: Any): -> Any

This means x can be of any type like strings, dict, list, etc

--------------------------------------------------------------------------------------------------------------

3. What is Databricks Lakebase Endpoint?

In Lakebase's hierarchy: Project -> Branch -> Endpoint


When we create a Lakebase project, Lakebase auto-creates a production branch with a primary read-write endpoint.

we can add more endpoints - e.g., a read-only endpoint for production data.

--------------------------------------------------------------------------------------------------------------

4. Models vs Services in Databricks Unity Catalog.


Model: databricks-gte-large-en

Service: Serving endpoints created with Models

--------------------------------------------------------------------------------------------------------------

5. w.postgres.get_endpoint(name=endpoint_name)

For example endpoint_name = f"projects/{LB_PROJECT}/branches/{LB_BRANCH}/endpoints/{LB_ENDPOINT}"

here LB_ENDPOINT can be primary(default), read-only endpoint

This function returns an object which contains host - needed for creation of connection to lakebase

example host: ep-lucky-forest-d16gs4rl.database.us-west-2.cloud.databricks.com


This value changes based on PROJECT, BRANCH and ENDPOINT values

--------------------------------------------------------------------------------------------------------------

6. What is trailing comma after last argument in function?

psycopg.connect(
    host=...,
    dbname=...,
    user=...,
    password=...,
    sslmode="require",  # ← this comma
)


This is helpful for git diffs cleaner.


Later, if we add 6th argument, only one line changes in diff instead of two


'''