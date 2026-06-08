'''
What is a Graph Database?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

A graph database is a type of NoSQL database that uses graph data structures (nodes, edges, and properties) to store, represent and query data.
Instead of storing data in tables (like relational databases) or documents (like document stores), it stores data as a network of relationships.


Core Components

    Node (Vertex)  - Represents an entity  - A Person, Movie, or Company
    Edge (Relationship) - Represents connection between nodes  -  FRIENDS_WITH, ACTED_IN, WORKS_AT
    Property   -    Attribute of node or edge   -   Age of Person in Node,   FIREDNS since 2020



Example

    (Alice:Person {age: 30}) --- [:FRIENDS_WITH {since:2015}]  -> (Bob:Person {age: 25})
            |
        [:WORKS_AT]  -> (Google:Company {industry: "Technology"})
--------------------------------------------------------------------------------------------------------------------------------------------------------------

why Graph Database?

1. Fast traversal - No expensive JOINs; 
2. Flexible Schema


Popular Graph Databases: Neo4j, Amazon Neptune, etc,.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The graph you see in the UI is a logical representation. Under the hood, nodes and edges are stored as records with IDs and metadata in the AWS distributed 
SSD storage system.


'''