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



What is Neptune Engine? which to be configured while creating Neptune DB instance.


    The Amazon Neptune Engine is the fully managed graph database software layer provided by AWS. It is software the executes queries, manages graph data, and enforces
transactions. we interact with it through Gremlin or SPARQL queries, while AWS handles the underlying infrastructure. Internally, the engine runs on EC2- like compute 
instances and stores data on SSD-backed storage, but those details are abstracted away - you only see the database endpoint.



Example value: Neptune 1.4.7.0.R1


-------------------------------------------------------------------------------------------------------------------------------------------------------------------


While creating Neptune DB, it asks for


    DB Cluster Name     - Whole Neptune cluster which contains Primary instance and replica instances

    DB Instance Name    - Individual database instance within the cluster.


    Example: social-graph-cluster

            social-graph-writer, social-graph-reader1




-------------------------------------------------------------------------------------------------------------------------------------------------------------------


QUery neptune Db

Based on the Sparql query

    Internally quads are built (:Subject, :Predicate, :Object, :Graph)

    Subject: The entity being described (e.g., Alice)
    Predicate: The property or relationship (e.g., knows)
    Object: The value or target entity (e.g., Bob)
    Graph: The named graph or context in which the triplet exists (e.g.,: SocialGraph)



Why quad matters? In Neptune indexing happens based on quads.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------


Use Property graphs - when focus is on relationships with attributes


Use RDF graphs - when focus is on semantic meaning, data integration.




'''