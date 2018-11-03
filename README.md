# gogs-migration
Migrating projects from Gitlab to Gogs - both repos and wikis (eventually)

## Can Do
Read the project list from Gitlab 
Create new project in Gogs under the specified owner

## Cant do yet
Migrate the code
Migrate the issues
Migrate the Wiki

## Usage
./main.py -?
usage: Migrate projects (repos & Wikis) from Gitlab to Gogs
       [-h] [-glp GITLABPAT] [-gl GITLABURL] [-go GOGSURL] [-goo GOGSOWNER]
       [-gop GOGSPAT] [-tmp TEMPDIR]
