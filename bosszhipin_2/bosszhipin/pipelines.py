# author：--Vincent--
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .items import BosszhipinItem,ZhiPinUrlItem
from scrapy.conf import settings

class BosszhipinPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname=settings['MONGODB_DBNAME']

        client = pymongo.MongoClient(host,port)
        db = client[dbname]
        self.post1 = db[settings['MONGODB_DOCNAME1']]
        self.post2= db[settings['MONGODB_DOCNAME2']]



    def process_item(self, item, spider):
        if isinstance(item,ZhiPinUrlItem):
            self.post1.insert(dict(item))
        elif isinstance(item,BosszhipinItem):
            self.post2.insert(dict(item))
        return item



