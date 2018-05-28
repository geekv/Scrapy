# author：--Vincent--
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader
import datetime

class BossJobItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()



def return_value(value):
    return value



def handle_time(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return str(create_date)

class BosszhipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    company_name=scrapy.Field()
    company_statuses=scrapy.Field()
    company_address=scrapy.Field(

    )
    company_type=scrapy.Field()
    company_web=scrapy.Field()
    public_data=scrapy.Field(
        # input_processor = MapCompose(handle_time)
    )
    salary=scrapy.Field()
    job_name=scrapy.Field()
    job_describe=scrapy.Field(
        output_processor=MapCompose(return_value)
    )


class ZhiPinUrlItem(scrapy.Item):
    job_name=scrapy.Field()
    company_name=scrapy.Field()
    jobs_url=scrapy.Field()
    next_url=scrapy.Field()