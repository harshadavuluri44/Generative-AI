'''

@lru_chache = Least Recently Used cache
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


@lru_cache is a decorator in Python's functools module that adds memoization (caching) to a function.


How it works ?


* When we decorate a function with @lru_cache, Python stores the results of function calls in memory.

* If the same function is called again with same arguments, Python returns the cache result instead of recomoputing.

* The "least recently used" part means that if the cache reaches its maximum size, the oldest unused results are discared to make room for new ones.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Example:


import sqlite3
from functools import lru_cache

conn = sqlite3.connect('example.db')


@lru_cache(maxsize=32)
def get_customer_orders(customer_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE customer_id= ?", (customer_id,))
    return cursor.fetchall()



orders_1 = get_customer_orders(101)

orders_2 = get_customer_orders(101)


'''