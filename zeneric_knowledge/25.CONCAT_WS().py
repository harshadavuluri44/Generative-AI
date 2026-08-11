'''

CONCAT_WS() stands for Concatenate With Separator. It joins multiple strings together using a specified spearator, and automatically skips NULL values.


syntax:   CONCAT_WS(separator, string1, string2, ...., stringN)



Example:


SELECT CONCAT_WS(', ', 'Nike', 'Swoosh', 'Catalog')

    'Nike, Swoosh, Catalog'


'''