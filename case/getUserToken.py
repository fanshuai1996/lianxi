import os
import sys
import requests
import allure
from case.login import Login

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class GetUserToken():
    def __init__(self,s,host):
        self.s = s
        self.host = host
        self.url = host + '/ecmps/getUserToken'

    @allure.step('获取用户token')
    def getUserToken(self,appid):
        data = {'appId':appid}
        r = self.s.get(url=self.url,params=data).json()
        return r

    @allure.step('获取真正的token')
    def getToken(self,appid):
        r = self.getUserToken(appid=appid)
        real_token = r['data']['token']
        return real_token


if __name__ == '__main__':
    s = requests.session()
    host = 'https://backstageservices.dreawer.com'
    l = Login(s,host)
    token, appid = l.getTokenAndAppID()
    h = {
        'appid':appid,
        'Authorization':token}
    s.headers.update(h)
    getToken = GetUserToken(s,host)
    real_token = getToken.getToken(appid=appid)
    print(real_token)
