
import pycurl
from io import BytesIO
from urllib.parse import urlencode


class CurlClient:

    def __init__(self):
        self.statichttpheaders = []

    def addStaticHeader(self, header):
        self.statichttpheaders.append(header)

    def Get(self, url, headers=[]):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HTTPHEADER, self.statichttpheaders + headers)
        c.perform()
        status = c.getinfo(pycurl.HTTP_CODE)
        c.close()

        body = buffer.getvalue()
        return status, body.decode('iso-8859-1')

    def Post(self, url, data, headers=[]):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HTTPHEADER, self.statichttpheaders + headers + ['Content-Type: application/json'])
        c.setopt(c.POST, 1)
        c.setopt(c.POSTFIELDS, data)
        #c.setopt(c.VERBOSE, True)
        c.perform()
        status = c.getinfo(pycurl.HTTP_CODE)
        c.close()

        body = buffer.getvalue()
        return status, body.decode('iso-8859-1')
