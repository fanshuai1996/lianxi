# coding=utf8
import os
import sys
import requests


class UploadImage():
    def __init__(self,s,host):
        self.s=s
        self.host=host
        self.url = host+'/ic/uploadImage'

    def uploadImage(self,file_path):
        file_name=os.path.split(file_path)[1]
        data={
            'appname':'RETAIL',
            'type':'IMAGE'
        }
        files={
            'files':(file_name,open(file_path,'rb'),'image/jpeg')
        }
        r=self.s.post(url=self.url,data=data,files=files).json()
        return  r

    def getImagePath(self, file_path):
        r = self.uploadImage(file_path)
        image_path = r['data'][0]
        return image_path

if __name__ == '__main__':
    s = requests.session()
    host = 'https://backstageservices.dreawer.com'
    file_path = './../image/image.png'
    image = UploadImage(s,host).getImagePath(file_path)
    print(image)





