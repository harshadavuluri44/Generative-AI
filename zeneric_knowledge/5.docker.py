'''
DOCKER
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Docker is an open-source platform that lets us package applications and their dependencies into lightweight, portable units called containers, ensuring they run 
consistently across different environments.

* Dockerfile contains all the dependency versions and requirements to run the application.
* Image is generated from the Dockerfile in the repo.
* If we run the above image on a host system, it becomes a container.
* With the help of a single image, we can create multiple containers.

Dockerfile contains the logic of installing requirements, copying the backend code, and what hosts can hit this backend code.

docker build : packs the whole backend code, installs requirements and freezes everything into an image.
docker run   : creates a container which starts the server (providing RAM, CPU etc).

----------------------------------------------------------------------------------------------------------------------------------------------------------------

FROM
====

FROM python:3.11-slim AS base

Every Dockerfile must start with FROM.

Code needs a Python interpreter and a Linux userland to run. A bare container built from a Docker image has neither,
so the FROM python:3.11-slim image supplies both.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

ENVIRONMENT VARIABLES
=====================

Environment variables in Docker/K8s work the same as in a Databricks App.

ENV TTD_TENANTS_DIR=/app/configs/tenants

The above env var is used by the source code of talk_to_data.

Flow:
    - ENV vars are stored in the image's metadata while creating the image.
    - When the container starts, every ENV from the image becomes part of the process environment.
      uvicorn starts with TTD_TENANTS_DIR already set.
    - The app's code reads them via os.getenv, usually once at startup. Values don't change per request.

We can set ENVs in the Dockerfile and in K8s too.

    Dockerfile has ENV_1, ENV_2, ENV_3
    K8s has        ENV_4, ENV_2, ENV_5

Both the Dockerfile and K8s have an env named ENV_2.

    - During image creation, the ENV_2 value is from the Dockerfile.
    - When the container starts, the ENV_2 value is overridden by the K8s yamls.

------------------------------------------------------------------------------------------------------------------------

RUN, WORKDIR, COPY
==================

RUN
    Executes a shell command while the image is being built, and saves the result into the image.


WORKDIR /app
    Creates the app folder and makes it the current working directory.
    All the commands that follow (RUN installing packages, COPY copying source code) reside under the /app folder.
    WORKDIR is similar to: mkdir /app + cd /app


COPY pyproject.toml ./
    Copies pyproject.toml into the root location of the /app folder (/app/pyproject.toml).


COPY src ./src
    Copies the src folder into the src folder under /app (if it doesn't exist, it gets created).


----------------------------------------------------------------------------------------------------------------------------------------------------------------

CMD
===

CMD ["uvicorn", "talk_to_data.api.app:app", "--host", "0.0.0.0", "--port", "8080"]

CMD defines the default command to run when a container starts from this image.
It does not run during the build, unlike RUN.

uvicorn
    A web server that sits between the network (port) and our source code.
    Our FastAPI code only defines what should happen for each request. It can't listen on a network port by itself.
    Uvicorn opens the port, accepts HTTP requests, and hands them to our code.


talk_to_data.api.app:app
    Tells uvicorn which code to run.
    talk_to_data.api.app -> src/talk_to_data/api/app.py (with dots instead of slashes)
    :app                 -> the name of the variable inside the above file, the FastAPI object.


--host 0.0.0.0
    Listen to traffic from outside the container too.
--host 127.0.0.1
    Accepts requests only from inside the container.


'''
