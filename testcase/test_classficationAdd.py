# coding=utf8
import pytest
import pytest_html
import random,os
import requests
import allure
from common.user_mysql import UserMysql
from common.mylogger import logger
from common.read_yaml import readYaml
from case.classficationDele import ClassficationDete


@allure.feature('分类管理模块')
class TestClassficationAdd():
    @allure.story('正常添加分类')
    @pytest.mark.parametrize('status', ['DEFAULT'])
    @pytest.mark.parametrize('name', ['fanser111'])
    @pytest.mark.parametrize('recommend', [True])
    @pytest.mark.parametrize('source', ['RETAIL'])
    def test_classficationAdd_true(self,status,name,recommend,source,getLogo,getSession,getYaml):
        logo=getLogo
        data={
            "parentId": "0",
            "status":status,
            "storeId": "1514e1d61686438f95fa46f19070c126",
            "name": name,
            "sequence": 1,
            "logo": logo,
            "recommend": recommend,
            "source":source
        }
        url='https://backstageservices.dreawer.com/gc/classification/add'
        s=getSession
        r=s.post(url=url,json=data).json()
        print(r)
        assert r['comment'] == 'Completed successfully'
        assert r['code'] == '000000'
        id = r['data']
        host = getYaml['host']
        ClassficationDete(s, host).classficationDete(id)

    @allure.story('异常添加分类')
    @pytest.mark.parametrize('status',['DEFAULT', 'UNPUBLISHED','APPLIED','REMOVED'])
    @pytest.mark.parametrize('name',['fanser111',''])
    @pytest.mark.parametrize('recommend',[True,False])
    @pytest.mark.parametrize('source',['APPX-APPX','RETAIL'])
    def test_classficationAdd_false(self,status,name,recommend,source,getLogo,getSession,getYaml):
        logo=getLogo
        data={
            "parentId": "0",
            "status":status,
            "storeId": "1514e1d61686438f95fa46f19070c126",
            "name": name,
            "sequence": 1,
            "logo": logo,
            "recommend": recommend,
            "source":source
        }
        url='https://backstageservices.dreawer.com/gc/classification/add'
        s=getSession
        r=s.post(url=url,json=data).json()
        logger.info(f'此时的入参：\n{data} 和响应值{r}')
        assert r['comment'] == 'Completed successfully'
        assert r['code'] == '000000'
        id = r['data']
        host = getYaml['host']
        ClassficationDete(s, host).classficationDete(id)



