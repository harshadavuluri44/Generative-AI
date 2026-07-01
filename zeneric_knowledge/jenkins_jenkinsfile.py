'''

Understanding the Jenkinsfile structure.



pipeline {} - the container

It's like a class or a function definition in code. Jenkins won't recognize your CI/CD instructions unless they're wrapped in this block.
It's the entry point Jenkins looks for when it reads the file.


Without pipeline {}, Jenkins has no idea what to do with the file.


pipeline {
    // everything goes here
}

---------------------------------------------------------------------------------------------------------------------------------------------------


pipeline {
    agent any
}


agent -- where should this job run?


Jenkins works on a master + worker model:

        Jenkins Master (server)
                - worker node 1 (a machine/ container)
                - worker node 2 (a machine/ container)
                - worker node 3 (a machine/ container)


    The master manages the jobs; the agents (workers) actually execute the shell commands.


agent any = I don't care which worker runs this job - pick any available one.

---------------------------------------------------------------------------------------------------------------------------------------------------

pipeline {
    agent any

    options {
        timeout(time:30, unit: 'MINUTES')
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

}


options {} is the global job configuration block. Think of it as settings you set once that apply to the entire pipeline run - before any stage even starts.staticmethod

1. timeout(time:30, unit: 'MINUTES')

    Problem it solves: If a job takes longer than 30 minutes, it will be aborted.

2. timestamps()

    What it does: Prepends a timestamp to every line in the console log output.

    Without it:
        Starting setup.....
        Installing dependencies.....
        Done.

    
    with it:
        12:45:01 Starting setup.....
        12:45:03 Installing dependencies.....
        12:46:22 Done.

3. disableConcurrentBuilds()

    Case: Two developers push code at same time.

    Only one build of this pipeline runs at a time. If second one is triggered while one is running, it waits in a queue.


4. buildDiscarder(logRotator(numToKeepStr: '20'))


    Jenkins stores every build's logs, artifacts, and results on disk. After hundreds of builds, this eats up gigabytes of disk space on the Jenkins server.

    What it does: Automatically deletes old buils, keeping only last 20. Build #1 gets deleted when build #21 comes in.


---------------------------------------------------------------------------------------------------------------------------------------------------

pipeline {
    agent any

    options {}

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'staging', 'production'],
            description: 'Target Environment to deploy to'
        )

        booleanParam(
            name: 'SKIP_DEPLOY',
            defaultValue: false,
            description: 'If true, skip the Deploy stage (just build and run tests)'
        )

    }
}


parameters {} makes the pipeline interactive. Instead of hardcoding values, you let the person triggering the build choose options at runtime - like a form that appears before the job runs.


What it looks like in Jenkins UI?


When someone clicks "Build with Parameters" in the Jenkins UI, they see the options

they pick their options, click build and params.ENVIRONMENT, etc. are available throughout the pipeline.

---------------------------------------------------------------------------------------------------------------------------------------------------

pipeline {
    agent any

    options {}

    parameters {}

    environment {
        PYTHONDONTWRITEBYTECODE = '1'
        PIP_NO_CACHE_DIR        = '1'
        SERVICE_DIR             = 'ingestion'
        PYTHONPATH              = "${WORKSPACE}/${SERVICE_DIR}"
    }
}



environment {} is where you define environment variables that are available to every stage in the pipeline - like how we give variable to databricks cluster


these variables are injected into every sh command across every stage automatically. We don't need to re-export them in each stage.staticmethod


---------------------------------------------------------------------------------------------------------------------------------------------------

pipeline {
    agent any

    options {}

    parameters {}

    environment {}

    stages {

        stage('name'){
            script/ sh logic
        }
    }

}



'''