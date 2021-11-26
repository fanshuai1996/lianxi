import os
import sys
import requests
import allure

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from case.login import Login
from case.getUserToken import GetUserToken

def getSession(host):
    s = requests.session()
    l = Login(s,host)
    token,appid = l.getTokenAndAppID()
    h = {
        'appid':appid,
        'Authorization':token}
    s.headers.update(h)
    get_token = GetUserToken(s,host)
    real_token = get_token.getToken(appid=appid)
    h = {'Authorization':real_token}
    s.headers.update(h)
    return s

if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'

    s = getSession(host=host)
    print(s.headers)