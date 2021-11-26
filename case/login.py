import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class Login():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/ecmps/login'

    def login(self,phoneNumber,password):
        data = {"phoneNumber":phoneNumber,"password":password}
        r = self.s.post(url=self.url,json=data).json()
        return r

    def getTokenAndAppID(self,phoneNumber='15527060286',password='hbc23687'):
        r = self.login(phoneNumber,password)
        token = r['data']['token']
        appid = r['data']['apps'][0]['appId']
        return token,appid

if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'

    s = requests.session()
    l = Login(s,host)
    token,appid = l.getTokenAndAppID()
    print(token,appid)


