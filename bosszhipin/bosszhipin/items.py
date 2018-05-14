# -*- coding: utf-8 -*-
# author：--Vincent--
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join









class BosszhipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    company_name=scrapy.Field()
    company_statuses=scrapy.Field()
    company_address=scrapy.Field(

    )
    company_type=scrapy.Field()
    company_web=scrapy.Field()
    public_data=scrapy.Field()
    salary=scrapy.Field()
    job_name=scrapy.Field()
    job_describe=scrapy.Field( )


class ZhiPinUrlItem(scrapy.Item):
    job_name=scrapy.Field()
    company_name=scrapy.Field()
    jobs_url=scrapy.Field()
    next_url=scrapy.Field()