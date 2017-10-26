# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# import pymongo

class TencentSpiderPipeline(object):
    def __init__(self):
        # self.client=pymongo.MongoClient('192.168.1.106',27017)
        # tencent=self.client['tencent']
        # self.zhaopin1=tencent['zhaopin1']

        #链接mysq数据库
        self.conn=pymysql.connect(host='192.168.1.106',user='root',passwd='root',db='tencent1',charset='utf8')
    def process_item(self, item, spider):
        for j in range(0,len(item['name'])):
            try:
                name=item['name'][j]
                info=item['info'][j]
                num=item['num'][j]
                location=item['location'][j]
                pubtime=item['pubtime'][j]
                link='hr.tencent.com/'+item['link'][j]
                #data部分是为了使用mongodb
                # data={
                #     'name':name,
                #     'info':info,
                #     'num':num,
                #     'location':location,
                #     'pubtime':pubtime,
                #     'link':link
                # }
                #使用mongodb数据库存储
                # self.zhaopin1.insert(data)

                #使用mysql数据库存储
                sql="insert into zhaopin(name,info,num,location,pubtime,link) values('"+name+"','"+info+"','"+num+"','"+location+"','"+pubtime+"','"+link+"')"
                self.conn.query(sql)
            except Exception as e:
                print(e)
        return item
    def close_spider(self):
        #关闭mysql数据库
        self.conn.close()
        #关闭mongodb数据库
        # self.client.close()
