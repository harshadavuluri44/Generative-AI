'''

CONCAT_WS() stands for Concatenate With Separator. It joins multiple strings together using a specified spearator, and automatically skips NULL values.


syntax:   CONCAT_WS(separator, string1, string2, ...., stringN)



Example:


SELECT CONCAT_WS(', ', 'Nike', 'Swoosh', 'Catalog')

    'Nike, Swoosh, Catalog'
-------------------------------------------------------------------------------------------------------------------------------------------------------


ARRAY_JOIN() is a SQL function that concatenates the elements of an array into a single string, with a specified delimiter between each element.


Syntax:

        ARRAY_JOIN(array, delimiter, null_replacement)

        null replacement - optional (string to use in place of NULL elements); if omitted, NULL elements are skipped.



SELECT ARRAY_JOIN(ARRAT('a','b','c'), ',')

    'a,b,c'



------------------------------



AARAY_JOIN() 
'''