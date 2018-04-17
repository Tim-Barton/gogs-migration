#! /usr/bin/python

import argparse
from gitlabclient import GitlabClient
from gogsclient import GogsClient


def migrateProject(args):
    pass
    #create project on gogs (use migrate util?)
    #if wiki enabled, create wiki, migrate wiki

parser = argparse.ArgumentParser("Migrate projects (repos & Wikis) from Gitlab to Gogs")
parser.add_argument('-glp', '--gitlabpat', help="The Personal Access Token (PAT) for the Gitlab user")
parser.add_argument('-gl', '--gitlaburl', help="The base url of the gitlab instance")
parser.add_argument('-go', '--gogsurl', help="The base url of the gogs instance")
parser.add_argument('-goo', '--gogsowner', help="The owner on gogs that all the projects to be migrated to")
parser.add_argument('-gop', '--gogspat', help="The Personal Access Token (PAT) for the Gogs user")
args = parser.parse_args()

gitlab = GitlabClient(args)

projects = gitlab.getAllGroupProjects()

#print(projects)
    
gogs = GogsClient(args)

if not gogs.checkIfOwnerExists(args.gogsowner):
    print("You need to create organisation/user {} in order to proceed with migration".format(args.gogsowner))
