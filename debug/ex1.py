# coding=utf8

import os
from common.mylogger import logger
from common.read_yaml import readYaml
from common.user_mysql import UserMysql


def pytest_addoption(parser):
    parser.addoption(
        '--environment', action='store''', default='test', help='运行环境选择：test/pro，默认test环境'
    )
    print(parser)

def environment(request):
    os.environ['environment'] = request.config.getoption('--environment')
    print(environment)
    logger.info('当前运行环境：%s'%os.environ['environment'])
    return os.environ['environment']

def file_path(environment):
    env = environment
    file_path = readyml(yamlFilePath)[env]['file_path']
    return eval(file_path)



if __name__ == '__main__':
    pytest_addoption()