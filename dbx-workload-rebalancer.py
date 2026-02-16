'''


Config
No-ownership-transfer
Fallback-sp
GitHub-token



Detect-all-artifacts:

    Scans the source databricks workspace for all 13 workspace-level-artifact types belonging to the team 
    (if —team-name is provided) or all teams.

    Generates a prioritised migration plan but does not actually migrate anything.

    Prints a comprehensive summary showing each artifact's name, confidence score, and migration priority.

    It's useful for previewing what would be migrated before running an actual migration.

---------------------------------------------------------------------------------------------------------------------------------


detect-only

scans only types we pass via --artifact-types, or all 13 if none specified.


    later again filter, --artifact-names, artifact-id's 

---------------------------------------------------------------------------------------------------------------------------------

brickflow-only

    detection and migration. but only for brickflow workflows

    if a team_name was provided, the detection is scoped to that team.

---------------------------------------------------------------------------------------------------------------------------------

Asset-bundle-only

    fetches all jobs from source workspace and excludes jobs that belong to Brickflow workflows.

---------------------------------------------------------------------------------------------------------------------------------


args.artifact_types or args.artifact_names or args.artifact_ids

    migrates specified or mentioned artifacts/objects

---------------------------------------------------------------------------------------------------------------------------------

else

    migrates all 13 types objects.

---------------


PROCESS FOR TESTING

1. detect-only as true

    pass artifact-type as cluster etc, pass artifact-names as cluster name, artifact-id as cluster id

2. Detect-all-artifacts as true

    scans all 13 artifacts for a specific team.

3. 

'''