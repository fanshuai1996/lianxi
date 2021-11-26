# coding=utf8

import random
import requests
import allure
from case.uploadImage import UploadImage
from case.getSession import getSession


class ClassficationAdd():
    def __init__(self,s,host):
        self.s = s
        self.host = host
        self.url = host + '/gc/classification/add'

    @allure.step('添加分类')
    def classficationAdd(self,logo):
        data={
            "parentId": "0",
            "status": "DEFAULT",
            "storeId": "1514e1d61686438f95fa46f19070c126",
            "name": f"这是{random.randint(1,1000)}",
            "sequence": 1,
            "logo": logo,
            "recommend": True,
            "source": "RETAIL"
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
    logo=UploadImage(s,host).getImagePath('../image/image.png')
    ClassficationAdd(s,host).classficationAdd(logo)



