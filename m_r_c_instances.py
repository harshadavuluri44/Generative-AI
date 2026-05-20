'''

In AWS EC2 and Databricks clusters, M, R, and C instance families mainly differ by CPU-to-memory balance.



M series = general purpose

    Balanced CPU and memory. Good default for mixed workloads: ETL, notebooks, moderate spark jobs, general Databricks jobs.


R series = memory optimized

    More RAM per vCPU. Better for Spark jobs with large shuffles, joins, caching, wide transformations, large pyspark operations or workloads that spill to disk/ hit OOM.


C series = compute optimized


    More CPU per dollar, less memory per CPU. Better for CPU-heavy workloads: UDF-heavy workloads, long running jobs - fast compute when data fits in memory.


'''