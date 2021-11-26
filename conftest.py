# coding=utf8
import os
import sys
import requests
import pytest
from common.read_yaml import readYaml
from common.user_mysql import UserMysql
from common.mylogger import logger



def pytest_addoption(parser):
    parser.addoption(
        '--environment', action='store''', default='pro', help='运行环境选择：test/pro，默认test环境'
    )
curPath = os.path.dirname(__file__)
yamlFilePath = os.path.join(curPath, 'configuration/env.yml')

@pytest.fixture(scope='session')
def getYaml():
    yamlpath='./../configuration/config.yml'
    text=readYaml(yamlpath)
    return text

@pytest.fixture(scope='session')
def usesql(getYaml):
    db=getYaml['db']
    usersql=UserMysql(db)
    return usersql

@pytest.fixture(scope='session',autouse=True)
def environment(request):
    os.environ['environment'] = request.config.getoption('--environment')
    print('当前运行环境',os.environ['environment'])
    logger.info('当前运行环境：%s'%os.environ['environment'])
    return os.environ['environment']

@pytest.fixture(scope='session',autouse=True)
def file_path(environment):
    env = environment
    print('env=',env)
    file_abspath=os.path.dirname(__file__)
    filepath = readYaml(yamlFilePath)[env]['file_path']
    file_path=os.path.join(file_abspath,filepath)
    file_path=os.path.abspath(file_path)
    print('file_path=   @@@',file_path)
    return file_path


