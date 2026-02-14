'''
CLASS vs MODULE — When to use what?
=====================================

We write reusable functions and use them across multiple files.
These functions can live inside CLASSES or inside MODULES (packages).

The key question: do these functions share common state (data)?


WHEN TO PREFER A CLASS
-----------------------
Use a class when functions operate on SHARED STATE (common data).


WHEN TO PREFER A MODULE / PACKAGE
-----------------------------------
Use a module when functions are STATELESS — they just take input and return output.



--------


Add __init__.py in folder to make it module 

    do - import functions inside __init__.py

        do - from module import functions wherever required. 



'''