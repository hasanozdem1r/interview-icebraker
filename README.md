Interview Icebraker
===============

This repository contains a comprehensive list of interview questions that can assist you in securing your dream job.

## Prequsities

* Python 3.9 or above
* Python Poetry for dependency management

## Installation

Read the Docs offers free documentation hosting. We are connecting our MkDocs documentation with Read-the-Docs
Install dependencies
```
poetry install
```
Generate requirements.txt for read-the-docs
```
poetry export --format requirements.txt --output requirements.txt --without-hashes
```
Following command generates site with given data under docs/ directory so you can check locally files
```
mkdocs build --clean
```
MkDocs comes with a built-in dev-server that lets you preview your documentation as you work on it. 
Start the server by running the following command
```
mkdocs serve
```

