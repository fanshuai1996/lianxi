# coding=utf8
# coding=utf8

import random
import requests
import allure
from case.uploadImage import UploadImage
from case.getSession import getSession
from case.classficationAdd import ClassficationAdd


class ClassficationDete():
    def __init__(self,s,host):
        self.s = s
        self.host = host
        self.url = host + '/gc/classification/delete'

    @allure.step('添加分类')
    def classficationDete(self,id):
        data={
            "storeId":"1514e1d61686438f95fa46f19070c126",
            "id":id
        }
        r=self.s.post(url=self.url,json=data).json()
        print(r)
        return r

if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    s = getSession(host=host)
    id='1fc250707c904a06bb1c5a9af1f61086'
    ClassficationAdd(s,host).classficationAdd(id)



