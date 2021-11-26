# coding=utf8
import pytest
import pytest_html
import random
import requests
import allure
from common.user_mysql import UserMysql
from common.mylogger import logger

@allure.feature('商品模块')
class TestGoodsAdd():
    @pytest.fixture(scope='function')
    def delete_goods(self,name,usesql):
        usesql=usesql
        sql = f'delete from classification_add where classification_name="{name}"'
        usesql.userSql(sql)
        logger.info('删除添加的数据')

    @pytest.fixture(scope='function')
    def add_goods(self, name,status,source, usesql):
        usesql = usesql
        sql = f'''
            INSERT INTO classification_add (classification_name,status,logo,url,parentId,source)
                VALUES('{name}','{status}','/resource/RETAIL/20211119/e8e6c8b16ef842a681e4054f53be2725.png','','0','{source}'); 
        '''
        usesql.userSql(sql)
        logger.info('添加数据')

    @pytest.fixture(scope='function')
    def select_goods(self,name,usesql):
        usesql = usesql
        sql = f'''
                select * from classification_add where classification_name='{name}'
            '''
        data=usesql.userSql(sql)
        logger.info('挑选数据')
        return data


    @allure.story('正常商品添加')
    @pytest.mark.parametrize('name', ['这是1','这是2','这是3'])
    @pytest.mark.parametrize('stockType', ['UNRESTRICTED','RESTRICTED'])
    @pytest.mark.parametrize('status', ['DEFAULT','UNPUBLISHED'])
    @pytest.mark.parametrize('recommend', [True,False])
    @pytest.mark.parametrize('source', ['RETAIL'])
    @pytest.mark.parametrize('stock', [1100,0])
    @pytest.mark.parametrize('salesVolume', [123])
    @pytest.mark.parametrize('price', ["1234",""])
    @pytest.mark.parametrize('description', ['这是好的'])

    # @pytest.mark.parametrize('name',[ f'这是{i}' for i in range(1,4)])
    # @pytest.mark.parametrize('stockType', ['UNRESTRICTED','RESTRICTED'])
    # @pytest.mark.parametrize('status', ['DEFAULT', 'UNPUBLISHED','APPLIED','REMOVED'])
    # @pytest.mark.parametrize('recommend', [True,False])
    # @pytest.mark.parametrize('source', ['APPX-APPX', 'RETAIL'])
    # @pytest.mark.parametrize('stock', [1100,2200,3000])
    # @pytest.mark.parametrize('salesVolume', [3, 0])
    # @pytest.mark.parametrize('price', [10, 0])
    # @pytest.mark.parametrize('description', ['这是好的',''])
    def test_goodsAdd_true(self,name,stockType,status,recommend,source,stock
                  ,salesVolume,price,description,getSession,add_goods,select_goods,delete_goods):
        data={
                "storeId": "1514e1d61686438f95fa46f19070c126",
                "name": name,
                "categoryId": "bedbdf24503b11e8a3bc7cd30abc",
                "stockType": stockType,
                "mainFigure": "/resource/RETAIL/20211117/914e6a7ac79841b19b6509cef6d953ef.png",
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
        logger.info('{},{},{},{},{},{},{},{},{}'.format(name,stockType,status,recommend,source,stock
                  ,salesVolume,price,description))
        s=getSession
        logger.info('s={}'.format(s))
        url='https://backstageservices.dreawer.com/gc/goods/add'
        a=s.post(url=url,json=data)

        r=a.json()
        print(r)
        print(type(r))
        logger.info('该接口执行花费了{}s'.format(a.elapsed.total_seconds()))
        data=select_goods[0]
        logger.info(data)
        assert r['comment']=="Completed successfully"
        assert r['code']=='000000'
        assert data['classification_name']==name
        assert data['source']==source
        assert data['status']==status

    @allure.story('异常商品添加')
    @pytest.mark.parametrize('name', ['这是1', '这是2', '这是3'])
    @pytest.mark.parametrize('stockType', ['UNRESTRICTED', 'RESTRICTED'])
    @pytest.mark.parametrize('status', ['DEFAULT', 'UNPUBLISHED'])
    @pytest.mark.parametrize('recommend', [True, False])
    @pytest.mark.parametrize('source', ['APPX-APPX'])
    @pytest.mark.parametrize('stock', [1100, 0])
    @pytest.mark.parametrize('salesVolume', [123])
    @pytest.mark.parametrize('price', ["1234", ""])
    @pytest.mark.parametrize('description', ['这是好的'])
    # @pytest.mark.parametrize('name',[ f'这是{i}' for i in range(1,4)])
    # @pytest.mark.parametrize('stockType', ['UNRESTRICTED','RESTRICTED'])
    # @pytest.mark.parametrize('status', ['DEFAULT', 'UNPUBLISHED','APPLIED','REMOVED'])
    # @pytest.mark.parametrize('recommend', [True,False])
    # @pytest.mark.parametrize('source', ['APPX-APPX', 'RETAIL'])
    # @pytest.mark.parametrize('stock', [1100,2200,3000])
    # @pytest.mark.parametrize('salesVolume', [3, 0])
    # @pytest.mark.parametrize('price', [10, 0])
    # @pytest.mark.parametrize('description', ['这是好的',''])
    def test_goodsAdd_false(self, name, stockType, status, recommend, source, stock
                      , salesVolume, price, description, getSession, add_goods, select_goods, delete_goods):
        data = {
            "storeId": "1514e1d61686438f95fa46f19070c126",
            "name": name,
            "categoryId": "bedbdf24503b11e8a3bc7cd30abc",
            "stockType": stockType,
            "mainFigure": "/resource/RETAIL/20211117/914e6a7ac79841b19b6509cef6d953ef.png",
            "service": "Test",
            "status": status,
            "recommend": recommend,
            "source": source,
            "classificationIds": ["ca90efc41743422a9e3fd6429a1e5bd2", "86f94b0b2c3e4c789409410db66c9517"],
            "skus": [{
                "stock": stock,
                "salesVolume": salesVolume,
                "originalPrice": "223",
                "price": price,
                'description': description
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
        logger.info('{},{},{},{},{},{},{},{},{}'.format(name, stockType, status, recommend, source, stock
                                                        , salesVolume, price, description))
        s = getSession
        logger.info('s={}'.format(s))
        url = 'https://backstageservices.dreawer.com/gc/goods/add'
        a = s.post(url=url, json=data)
        r = a.json()
        print(r)
        print(type(r))
        logger.info('该接口执行花费了{}s'.format(a.elapsed.total_seconds()))
        data = select_goods[0]
        logger.info(data)
        assert r['comment'] == "Completed successfully"
        assert r['code'] == '000000'
        assert data['classification_name'] == name
        assert data['source'] == source
        assert data['status'] == status


