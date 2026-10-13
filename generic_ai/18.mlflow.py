'''
MLflow is an open-source platform for managing the end-to-end machine learning lifecylce.

* mlflow.set_registry_uri('databricks-uc')
    By setting "databricks-uc", your models will be registered under Unity Catalog - meaning when we later call mlflow.regsiter_model(....), the model is stored at a 
    path like published_domain.team_data_technology_foundation.my_model

* mlflow.set_experiment(path)
    This tells ML flow where to log training runs (metrics, parameters, artifacts)

* mlflow.trace()
    This is used to trace the end to end flow of the model.

    For example from a user prompt to getting back response of MCP service.


'''