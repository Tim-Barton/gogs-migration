#! /usr/bin/python

import argparse
from gitlabclient import GitlabClient


def migrateProject(args):
    pass
    #create project on gogs (use migrate util?)
    #if wiki enabled, create wiki, migrate wiki

parser = argparse.ArgumentParser("Migrate projects (repos & Wikis) from Gitlab to Gogs")
parser.add_argument('-p', '--pat', help="The Personal Access Token (PAT) for the Gitlab user")
parser.add_argument('-gl', '--gitlaburl', help="The base url of the gitlab instance")
parser.add_argument('-go', '--gogsowner', help="The owner on gogs that all the projects to be migrated to (must already exist)")
args = parser.parse_args()

gitlab = GitlabClient(args)

projects = gitlab.getAllGroupProjects()

print(projects)
    
