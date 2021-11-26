import os
import sys
import requests
import pytest
from case.login import Login
from case.getUserToken import GetUserToken
from case.uploadImage import UploadImage
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


@pytest.fixture(scope='module')
def getSession(getYaml):
    host =getYaml['host']
    print(host)
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

@pytest.fixture(scope='module')
def getLogo(file_path,getSession,getYaml):
    s=getSession
    host = getYaml['host']
    filepath=UploadImage(s,host).getImagePath(file_path)
    print(filepath)
    return filepath



# def uploadImage()


if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    s = getSession(host=host)
    print(s.headers)