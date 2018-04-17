
from curl import CurlClient
import json


class GitlabClient:

    def __init__(self, args):
        self.url = args.gitlaburl
        self.pat = args.gitlabpat
        self.curlClient = CurlClient()
        self.curlClient.addStaticHeader("Private-Token: {}".format(self.pat))

    def getAllGroupProjects(self):
        status, namespaceJson = self.curlClient.Get(self.url + "/api/v3" + "/namespaces")
        namespaces = json.loads(namespaceJson)
        groupNamespaces = [ namespace["id"] for namespace in namespaces if namespace["kind"] == "group"]

        status, projectsJson = self.curlClient.Get(self.url + "/api/v3" + "/projects")
        projects = json.loads(projectsJson)
        return [project for project in projects if project["namespace"]["id"] in groupNamespaces]
