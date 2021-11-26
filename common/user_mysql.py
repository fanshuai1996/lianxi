# coding=utf8
import pymysql
from common.mylogger import logger


class UserMysql():
    def __init__(self,dbinfo):
        self.dbinfo=dbinfo
        self.db=pymysql.connect(cursorclass=pymysql.cursors.DictCursor,**dbinfo)
        self.cursor=self.db.cursor()
    def userSql(self,sql):
        try:
            self.cursor.execute(sql)
            text=self.cursor.fetchall()
            if text:
                return text
            else:
                self.db.commit()
                print('提交成功')
                logger.info('提交成功')
        except Exception as e:
            print(e)
            logger.info(e)
            self.db.rollback()
    def close(self):
        # 关闭连接
        self.db.close()


if __name__ == '__main__':
    db = {
        'host': '192.168.1.24',
        'user': 'root',
        'password': '123456',
        'database': 'appx',
        'port': 3310
    }
    ab=UserMysql(db)
    sql1='''
        INSERT INTO classification_add (classification_name,`status`,logo,url,parentId,source)
                VALUES('coco1','DEFAULT','/resource/RETAIL/20211119/e8e6c8b16ef842a681e4054f53be2725.png','','0','APPX');
    '''
    sql2='''
        select * from classification_add
    '''
    data=ab.userSql(sql2)
    print(data)