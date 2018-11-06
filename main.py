#! /usr/bin/python

import argparse
import sys
from gitlabclient import GitlabClient
from gogsclient import GogsClient
import os
import git

def gogsIsPrivate(public, visibility_level):
    if public:
        return False
    elif visibility_level == 10: #found from experimentation that my 'Internal' repos have this value
        return False
    else:
        return True

parser = argparse.ArgumentParser("Migrate projects (repos & Wikis) from Gitlab to Gogs")
parser.add_argument('-glp', '--gitlabpt', help="The Private Token for the Gitlab user")
parser.add_argument('-gl', '--gitlaburl', help="The base url of the gitlab instance")
parser.add_argument('-go', '--gogsurl', help="The base url of the gogs instance")
parser.add_argument('-goo', '--gogsowner', help="The owner on gogs that all the projects to be migrated to")
parser.add_argument('-gop', '--gogspat', help="The Personal Access Token (PAT) for the Gogs user")
parser.add_argument('-tmp', "--tempdir", default="/tmp", help="Directory to use for temporary storage of artifacts during migration")
args = parser.parse_args()

gitlab = GitlabClient(args)
gogs = GogsClient(args)

print("Checking prerequisites")

if args.gogsowner is not None and not gogs.ownerOrgExists(args.gogsowner):
    print("You need to create organisation/user {} in order to proceed with migration".format(args.gogsowner))
    sys.exit(1)

print("Calculating Migration context")

gitlabProjects = gitlab.getAllGroupProjects() #ignoring user's personal projects
gogsProjects = gogs.getAllProjectsForOwner(args.gogsowner)
gogsProjectNames = [gogs.transformShortName(project["full_name"]) for project in gogsProjects ]
migrateProjects = [project for project in gitlabProjects if project["name"] not in gogsProjectNames ]

#for project in migrateProjects:
    #print(project["name"], project["public"], project["visibility_level"])

#print(migrateProjects)

print("Starting Migration")
for project in migrateProjects:
    print("Migrating {} as {}".format(project["name"], project["path"]))
    success, gogsProject = gogs.createProject(project["path"], project["description"], gogsIsPrivate(project["public"], project["visibility_level"]), args.gogsowner)
    if not success:
        print("Unable to create {}: {}\n".format(project["name"],gogsProject))
        continue # skip any more processing if we can't create the project
    print("\tMigrating git repo")
    #migrate git repo
    tempdir = args.tempdir + "/" + project["name"]
    if not os.path.exists(tempdir):
        os.mkdir(tempdir)
    repo = git.Repo.clone_from(project["ssh_url_to_repo"], tempdir, bare=True)
    
    print(gogsProject["ssh_url"])
    gogsRemote = repo.create_remote("Gogs", gogsProject["ssh_url"])
    gogsRemote.push(None, None, mirror=True)
    os.rmdir(tempdir)
    print("\tMigrating issues - not yet implemented")
    #migrate issues
    print("\tMigrating wiki - not yet implemented")
    #migrate wiki
    print("Migrated {} successfully\n".format(project["name"]))
    pass
    
print("Migration Complete")
