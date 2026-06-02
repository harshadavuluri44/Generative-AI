'''

Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets.


Neptune supports query languages like Gremlin,
                                      SPARQL
                                      W3C's RDF
                                      Neo4j's openCypher

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Neptune database is highly available, with read replicas, point-in-time recovery, continous backup to Amazon S3, and replication across availability zones.

    Read replica (max of 15 in addition to primrary DB instance)
        means an ADDITIONAL DATABASE INSTANCE that shares the same underlying distributed storage layer as the primary instance.
        No data duplication.

    Point-in-time Recovery(PITR)
        Neptune continously records changes (transaction logs) in its distributed storage system
        If something goes wrong (accidental deletion, corruption), we can roll back the database to the exact moment before issue.

    Continous backup to S3
        Neptune automatically backs up graph data Amazon S3 from Neptune's distributed storage system(the live source of graph data).

    Replication across availability zones in single aws region (stored in Distributed SSD storage system)
        Neptune replicates only graph data across multiple zones but not database is created.
        Db1 in zone 1 can access graph data in zone 2.



-------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can send API requests (HTTP POST) to Neptune's cluster endpoint, with the body containing queries written in one of the supported query languages.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------


Network Isolation with VPC


    Neptune is deployed inside Virtual Private Cloud (VPC)

    Only resources (EC2, Lambda, etc.) inside that VPC can send HTTP requests to Neptune's endpoints.


    HTTP request with SPARQL query language should run on EC2 instance which is registered with Neptune instance VPC.


By default, Neptune is not publicly accessible - meaning you cannot hit its HTTP endpoint directly from internet.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------


    






'''