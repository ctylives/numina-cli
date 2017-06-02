"""The hello command."""


from json import dumps
import requests
import datetime as dt
import urllib
from .base import Base
from . import utils

class Counts(Base):

    def run(self):
        token = utils.get_saved_token()
        if token == False:
            return
        if not token:
            print("No token saved, please provide an authentication token for the cli via the authenticate command")
            return    
        
        r = requests.get(self.request_url + '/b/devices', headers={ 'Authorization': 'JWT ' + token })
        print(r.text)
        is_expired = utils.check_if_expired(r)
        if not is_expired:
            print(r.text)
