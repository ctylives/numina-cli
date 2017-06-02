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
            
        if not '<feeds>' in self.options:
            print("Counts requires the feed option, please use feed_mongo_id from the devices endpoint to restrict your query")
            return

        params =    (  
                        ('feed',self.options["<feeds>"]),
                        ('bins',self.options.get("bins", '1h')),
                        ('starttime', self.options.get("starttime", (dt.datetime.utcnow() - dt.timedelta(days=7)).isoformat()) ),
                        ('endtime', self.options.get("endtime", dt.datetime.utcnow().isoformat()))
                    )

        r = requests.get(self.request_url + '/b/counts?' + urllib.parse.urlencode(params), headers={ 'Authorization': ' JWT ' + token })
        is_expired = utils.check_if_expired(r)
        if not is_expired:
            print(r.text)
