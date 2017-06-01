"""The hello command."""


from json import dumps
import requests
from .base import Base

class Movements(Base):

    def run(self):
        authfile = open('token.txt', 'r')
        token = authfile.read()
        token = token.replace('"', '')
        if not token:
            print("No token saved, please provide an authentication token for the cli via the authenticate command")
            return    
        
        print('Retrieving movements... ')
        r = requests.get(self.request_url + '/b/movements', headers={ 'Authorization': ' JWT ' + token })
        print(r.text)
        authfile.close()
