"""The hello command."""


from json import dumps
import requests
import datetime as dt
import urllib
from .base import Base
from . import utils

class Counts(Base):

    def run(self):
        authfile = open('token.txt', 'r')
        token = authfile.read()
        token = token.replace('"', '')
        authfile.close()
        if not token:
            print("No token saved, please provide an authentication token for the cli via the authenticate command")
            return    
            
        if not '<org_id>' in self.options:
            print("Devices requires the org_id option, use the feed_mongo_id in the device result object in other commands")
            return

        params =    (  
                        ('org_id',self.options["<org_id>"]),
                    )

        r = requests.get(self.request_url + '/b/devices?' + urllib.parse.urlencode(params), headers={ 'Authorization': ' JWT ' + token })
        is_expired = utils.check_if_expired(r)
        if not is_expired:
            print(r.text)
