# coding=utf8

import os
import yaml


def readYaml(yamlpath):
    if not os.path.isfile(yamlpath):
        raise FileNotFoundError("文件不存在，请检查是否存在该文件: %s"%yamlpath)
    f=open(yamlpath,'r',encoding='utf8').read()
    text=yaml.load(f,Loader=yaml.FullLoader)
    return text


if __name__ == '__main__':
    yamlpath='./../configuration/config.yml'
    text=readYaml(yamlpath)
    print(text)


