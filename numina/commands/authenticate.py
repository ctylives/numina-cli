"""The authetication command."""


from json import dumps
import requests
from .base import Base
import os

class Authenticate(Base):

    def run(self):
        authfile = open(os.path.expanduser('~') + '/.numina-token.txt', 'w')
        if not '<token>' in self.options:
            print("please provide an authentication token")
            return    
        
        print('\n Authentication token has been saved for future use: ' + dumps(self.options["<token>"]))
        authfile.write(dumps(self.options["<token>"]))
        authfile.close()
