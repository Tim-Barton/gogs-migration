#! /usr/bin/python

import argparse
import sys
from gitlabclient import GitlabClient
from gogsclient import GogsClient


parser = argparse.ArgumentParser("Migrate projects (repos & Wikis) from Gitlab to Gogs")
parser.add_argument('-glp', '--gitlabpat', help="The Personal Access Token (PAT) for the Gitlab user")
parser.add_argument('-gl', '--gitlaburl', help="The base url of the gitlab instance")
parser.add_argument('-go', '--gogsurl', help="The base url of the gogs instance")
parser.add_argument('-goo', '--gogsowner', help="The owner on gogs that all the projects to be migrated to")
parser.add_argument('-gop', '--gogspat', help="The Personal Access Token (PAT) for the Gogs user")
parser.add_argument('-tmp', "--tempdir", default="/tmp", help="Directory to use for temporary storage of artifacts during migration")
args = parser.parse_args()

gitlab = GitlabClient(args)
gogs = GogsClient(args)

if args.gogsowner is not None and not gogs.ownerExists(args.gogsowner):
    print("You need to create organisation/user {} in order to proceed with migration".format(args.gogsowner))
    sys.exit(1)


gitlabProjects = gitlab.getAllGroupProjects()
gogsProjects = gogs.getAllProjectsForOwner(args.gogsowner)
gogsProjectNames = [gogs.transformShortName(project["full_name"]) for project in gogsProjects ]
migrateProjects = [project for project in gitlabProjects if project["name"] not in gogsProjectNames ]

print(migrateProjects)

for project in migrateProjects:
    #create gogs project with name
    #migrate git repo
    #migrate issues
    #migrate wiki
    pass
