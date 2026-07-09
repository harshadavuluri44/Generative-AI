'''

map<> vs struct<> Column Types in Databricks / Spark SQL
==================================================================================================================

MAP<string, string>
-------------------
Variable key-value pairs — keys can differ from row to row.

  Schema:   map<string, string>

  Example value:
    {"Abbreviation": "WOH", "Format Type": "Metric", "KPI": "Yes"}

  Access syntax:
    additional_metadata['Abbreviation']


STRUCT<...>
-----------
Fixed, named fields — same fields present in every row.

  Schema:   struct<abbreviation: string, format_type: string, kpi: string>

  Example value:
    {"abbreviation": "WOH", "format_type": "Metric", "kpi": "Yes"}

  Access syntax:
    additional_metadata.abbreviation


KEY DIFFERENCE
--------------
  map<>    → flexible schema; any keys per row; accessed via bracket notation
  struct<> → fixed schema; fields defined at table creation; accessed via dot notation
'''
