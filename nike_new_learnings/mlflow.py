'''
MLflow is an open-source platform for managing the end-to-end machine learning lifecylce.

* mlflow.set_registry_uri('databricks-uc')
    By setting "databricks-uc", your models will be registered under Unity Catalog - meaning when we later call mlflow.regsiter_model(....), the model is stored at a path like sole_eng_calc.default.my_model

* mlflow.set_experiment(path)
    This tells ML flow where to log training runs (metrics, parameters, artifacts)


'''