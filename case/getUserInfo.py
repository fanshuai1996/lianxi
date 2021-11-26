import os
import sys
import requests
import allure
from case.getSession import getSession

sys.path.append('./..')

class GetUserInfo():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/bsmc/user/getInfo'

    @allure.step('获取用户信息')
    def getUserInfo(self,proxies=None):
        r = self.s.get(url=self.url).json()
        return r


if __name__ == '__main__':
    print(sys.path)
    host = 'https://backstageservices.dreawer.com'

    s = getSession(host=host)
    info = GetUserInfo(s,host)
    r = info.getUserInfo()
    print(r)