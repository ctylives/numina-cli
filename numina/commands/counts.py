"""The hello command."""


from json import dumps
import requests
from .base import Base

class Counts(Base):

    def run(self):
        authfile = open('token.txt', 'r')
        token = authfile.read()
        token = token.replace('"', '')
        if not token:
            print("No token saved, please provide an authentication token for the cli via the authenticate command")
            return    
        
        print('Retrieving counts... ')
        r = requests.get(self.request_url + '/b/counts', headers={ 'Authorization': ' JWT ' + token })
        print(r.text)
        authfile.close()
