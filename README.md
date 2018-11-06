# gogs-migration
Migrating projects from Gitlab to Gogs - both repos and wikis (eventually)

This was developed to migrate from Gitlab 7.X to Gogs v0.11 via a mix of API references and experimentation.
Your usage for different versions may vary

## Prerequisites

* Python 3.X ( I'm using 3.7 - your usage may vary)
 * The scripts expect /usr/bin/python to be this version as per the usage below
* PyCurl installed
* GitPython installed
* SSH Keys set up for Gitlab & Gogs, such that a `git clone repo_url` will succeed (i.e. it's the default key )
 * Ensure that you have SSH cloned or otherwise interacted with the server to the key fingerprint has been saved

## Can Do
Read the project list from Gitlab 
Create new project in Gogs under the specified owner
Migrate the code

## Cant do yet
Migrate the issues
Migrate the Wiki

## Usage
./main.py -?
usage: Migrate projects (repos & Wikis) from Gitlab to Gogs
       [-h] [-glp GITLABPAT] [-gl GITLABURL] [-go GOGSURL] [-goo GOGSOWNER]
       [-gop GOGSPAT] [-tmp TEMPDIR]
