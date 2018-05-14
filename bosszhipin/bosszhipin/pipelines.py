# -*- coding: utf-8 -*-
# author：--Vincent--
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pdb
from .items import BosszhipinItem,ZhiPinUrlItem
from scrapy.conf import settings


#数据库连接
class BosszhipinPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname=settings['MONGODB_DBNAME']

        client = pymongo.MongoClient(host,port)
        db = client[dbname]
        self.post1 = db[settings['MONGODB_DOCNAME1']]
        self.post2= db[settings['MONGODB_DOCNAME2']]
    #     self.mongo_url=mongo_url
    #     self.mongo_db=mongo_db
    #
    # @classmethod
    # def from_crawler(cls,crawler):
    #     return cls(
    #         mongo_url=crawler.settings.get('MONGO_URL'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE','bosszp')
    #     )
    #
    # def open_spider(self,spider):
    #     self.client = pymongo.MongoClient(self.mongo_url)
    #     self.db = self.client[self.mongo_db]
    #     print('nihao')

    # def close_spider(self, spider):
    #     self.client.close()

    #插入数据库
    def process_item(self, item, spider):
        if isinstance(item,ZhiPinUrlItem):
            self.post1.insert(dict(item))
        elif isinstance(item,BosszhipinItem):
            self.post2.insert(dict(item))
        return item

    #     if isinstance(item,BosszhipinItem):
    #         self._process_detail_item(item)
    #     elif isinstance(item,ZhiPinUrlItem):
    #         self._process_summary_item(item)
    #     return item
    #
    # def _process_detail_item(self,item):
    #     self.db.JobsInfo.insert(dict(item))
    #
    # def _process_summary_item(self,item):
    #     self.db.summary.insert(dict(item))

