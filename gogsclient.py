from curl import CurlClient
import json

class GogsClient:

    def __init__(self, args):
        self.url = args.gogsurl + "/api/v1/"
        self.pat = args.gogspat
        self.curlClient = CurlClient()
        self.curlClient.addStaticHeader( "Authorization: token {}".format(self.pat))
        
    def getAllProjects(self):
        status, projectsJson = self.curlClient.Get(self.url + "user/repos")
        return json.loads(projectsJson)
        
    def getAllProjectsForOwner(self, owner=None):
        if owner is not None:
            status, projectsJson = self.curlClient.Get(self.url + "orgs/{}/repos".format(owner))
        else:
            status, projectsJson = self.curlClient.Get(self.url + "user/repos")
        if status == 200:
            return json.loads(projectsJson)
        else:
            return []
        
    def ownerOrgExists(self, owner):
        status, orgsJson = self.curlClient.Get(self.url + "user/orgs")
        orgs = json.loads(orgsJson)
        return owner in [org["username"] for org in orgs]
        
    def transformShortName(self, fullname):
        return fullname[fullname.find('/'):]
        
    def createProject(self, name, description, private, owner=None):
        projectInfo = { "name": name,
                        "description" : description,
                        "private" : private}
        projectInfoJson = json.dumps(projectInfo)
        if owner is not None:
            status, returnJson = self.curlClient.Post(self.url + "org/{}/repos".format(owner), projectInfoJson)
        else:
            status, returnJson = self.curlClient.Post(self.url + "user/repos", projectInfoJson)
        if status == 201:
            return True, json.loads(returnJson)
        else:
            return False, json.loads(returnJson)["message"]
