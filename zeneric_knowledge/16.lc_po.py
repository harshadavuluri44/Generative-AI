'''

In LIQUID CLUSTERING, clustering columns are fixed(user-defined) and optimization happens incrementally.

In PREDICTIVE OPTIMIZATION, Databricks identifies hot columns and automatically chooses clustering columns, then runs
optimization using Liquid clustering.



NOTE - LC and PO are at file level not at folder level like PARTITIONING


----------


SCENARIO: Table A has 100 columns (c1,c2,...,c100)
    Partitioned by c1
    Liquid clustering on c2,c3

    Assume predictive optimization is enabled and databricks identifies c2,c4 as hot columns then again Liquid clustering
    takes place

    CLUSTER BY (c2, c4)





If hot columns are known enable Liquid clustering and ignore Predictive Optimization.


Ignore both if tables are small and cold tables.


VACCUM doesn't impact SQL query execution time.


'''