# coding=utf8
import json
import requests
import allure
from case.uploadImage import UploadImage
from getSession import getSession



class GoodsAdd():
    def __init__(self,s,host):
        self.s=s
        self.host=host
        self.url=self.host+'/gc/goods/add'

    @allure.step('添加商品')
    def goodsAdd(self,name,categoryId,stockType,mainFigure,status,recommend,source,stock
                  ,salesVolume,price,description):
        data={
                "storeId": "1514e1d61686438f95fa46f19070c126",
                "name": name,
                "categoryId": categoryId,
                "stockType": stockType,
                "mainFigure": mainFigure,
                "service": "Test",
                "status":status,
                "recommend": recommend,
                "source":source,
                "classificationIds": ["ca90efc41743422a9e3fd6429a1e5bd2", "86f94b0b2c3e4c789409410db66c9517"],
                "skus": [{
                    "stock": stock,
                    "salesVolume": salesVolume,
                    "originalPrice": "223",
                    "price": price,
                    'description':description
                }],
                "goodsPropertyNames": [],
                "freightParam": {
                    "type": "FIXED",
                    "price": "12",
                    "freightTemplateId": ""
                },
                "allowRefund": True,
                "express": True,
                "cityDistribution": False,
                "selfPickUp": False,
                "detail": None
            }
        print(data)
        print(type(data))
        r=self.s.post(url=self.url,json=data)
        print(r.text)
        return r

if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    file_path = './../image/image.png'

    s = getSession(host=host)
    mainFigure=UploadImage(s,host).getImagePath(file_path)
    data={
        "name":"你是新报",
        "categoryId":"bedbdf24503b11e8a3bc7cd30abc",
        "stockType":"RESTRICTED",
        "mainFigure":mainFigure,
        "status":"DEFAULT",
        "recommend":True,
        "source":"RETAIL",
        "stock":"10000",
        "salesVolume":123,
        "price":"1234",
        "description":"这是一款新的皮肤",
    }
    GoodsAdd(s,host).goodsAdd(**data)


