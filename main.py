#! /usr/bin/python

import pycurl
from io import BytesIO
import argparse
import json


def curlGet(url, pat):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HTTPHEADER, ["Private-Token: {}".format(pat)])
    c.perform()
    c.close()

    body = buffer.getvalue()
    # Body is a byte string.
    # We have to know the encoding in order to print it to a text file
    # such as standard output.
    return c.getinfo(pycurl.HTTP_CODE), body.decode('iso-8859-1')


def getGitlabGroupProjects(args):
    status, namespaceJson = curlGet(args.gitlaburl + "/api/v3" + "/namespaces", args.pat)
    namespaces = json.loads(namespaceJson)
    groupNamespaces = [ namespace["id"] for namespace in namespaces if namespace["kind"] == "group"]

    status, projectsJson = curlGet(args.gitlaburl + "/api/v3" + "/projects", args.pat)
    projects = json.loads(projectsJson)
    return [project for project in projects if project["namespace"]["id"] in groupNamespaces]


parser = argparse.ArgumentParser("Migrate projects (repos & Wikis) from Gitlab to Gogs")
parser.add_argument('-p', '--pat', help="The Personal Access Token (PAT) for the Gitlab user")
parser.add_argument('-gl', '--gitlaburl', help="The base url of the gitlab instance")
args = parser.parse_args()

projects = getGitlabGroupProjects(args)
