"""The hello command."""


from json import dumps
import requests
import datetime as dt
import urllib
from .base import Base

class Movements(Base):

    def run(self):
        authfile = open('token.txt', 'r')
        token = authfile.read()
        token = token.replace('"', '')
        if not token:
            print("No token saved, please provide an authentication token for the cli via the authenticate command")
            return    

        params =    (  
                        ('feed',self.options["<feeds>"]),
                        ('format',"json"),
                        ('starttime', self.options.get("starttime", (dt.datetime.utcnow() - dt.timedelta(days=7)).isoformat()) ),
                        ('endtime', self.options.get("endtime", dt.datetime.utcnow().isoformat()))
                    )

        r = requests.get(self.request_url + '/b/movements?' + urllib.parse.urlencode(params) , headers={ 'Authorization': ' JWT ' + token })
        print(r.text)
        authfile.close()
