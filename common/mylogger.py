# coding=utf8
import logging
import os
import datetime

print(os.path.dirname(os.path.dirname(__file__)))
file_path=os.path.dirname(os.path.dirname(__file__))+'\log'
print(file_path)
if not os.path.exists(file_path):
    os.makedirs(file_path)
log_name=datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
log_path=os.path.join(file_path,log_name)
print(log_path)

def MyLogger(log_path):
    logger=logging.getLogger()
    logger.setLevel(level=logging.DEBUG)
    fh=logging.FileHandler(f'{log_path}',encoding='utf-8')
    fh.setLevel(level=logging.INFO)
    fmt=logging.Formatter(' %(asctime)s - %(name)s - %(levelname)s -  %(message)s')
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger
logger=MyLogger(log_path)