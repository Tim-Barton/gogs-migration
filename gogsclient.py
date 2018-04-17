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
        
    def getAllProjectsForOwner(self, owner):
        status, projectsJson = self.curlClient.Get(self.url + "user/{}/repos".format(owner))
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
        if owner is not None:
            status, returnJson = CurlClient.Post(self.url + "/org/{}/repos".format(owner), projectInfo)
        else:
            status, returnJson = CurlClient.Post(self.url + "/user/repos", projectInfo)
