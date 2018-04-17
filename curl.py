
import pycurl
from io import BytesIO


class CurlClient:

    def __init__(self):
        self.statichttpheaders = []

    def addStaticHeader(self, header):
        self.statichttpheaders.append(header)

    def curlGet(self, url, headers=[]):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HTTPHEADER, self.statichttpheaders + headers)
        c.perform()
        status = c.getinfo(pycurl.HTTP_CODE)
        c.close()

        body = buffer.getvalue()
        # Body is a byte string.
        # We have to know the encoding in order to print it to a text file
        # such as standard output.
        return status, body.decode('iso-8859-1')
