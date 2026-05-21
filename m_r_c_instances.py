'''

In AWS EC2 and Databricks clusters, M, R, and C instance families mainly differ by CPU-to-memory balance.



M series = general purpose

    Balanced CPU and memory. Good default for mixed workloads: ETL, notebooks, moderate spark jobs, general Databricks jobs.


R series = memory optimized

    More RAM per vCPU. Better for Spark jobs with large shuffles, joins, caching, wide transformations, large pyspark operations or workloads that spill to disk/ hit OOM.


C series = compute optimized


    More CPU per dollar, less memory per CPU. Better for CPU-heavy workloads: UDF-heavy workloads, long running jobs - fast compute when data fits in memory.


--------------------------------------------------------------------------------------------------------------------


M, R, C series has graviton enabled instances.


Graviton instances are ARM based CPUs, they are power-efficient and can be cheaper for the same performance of usual general instances/ CPUs.

--------------------------------------------------------------------------------------------------------------------


Fleet instances


    User selects a fleet category (M/R/C) and size (small, medium, large), not one exact AWS EC2 type like m5.xlarge or m6i.xlarge.


    Then Databricks/AWS chooses a suitable underlying EC2 instance from a pool of compatible types based on availability and capacity.

fleet instances can be spot or on-demand.


'''