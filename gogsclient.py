from curl import CurlClient
import json

class GogsClient:

    def __init__(self, args):
        self.url = args.gogsurl + "/api/v1/"
        self.pat = args.gogspat
        self.curlClient = CurlClient()
        self.curlClient.addStaticHeader( "Authorization: token {}".format(self.pat))
        
    def getAllProjects(self):
        return self.curlClient.Get(self.url + "user/repos")
        
    def checkIfOwnerExists(self, owner):
        status, orgsJson = self.curlClient.Get(self.url + "user/orgs")
        orgs = json.loads(orgsJson)
        status, userJson = self.curlClient.Get(self.url + "users/{}".format(owner))
        return owner in [org["username"] for org in orgs] or status == 200
