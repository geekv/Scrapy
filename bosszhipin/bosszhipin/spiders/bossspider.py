# -*- coding: utf-8 -*-
# author：--Vincent--

import scrapy

from scrapy.http import Request
from bosszhipin.items import ZhiPinUrlItem,BosszhipinItem
from urllib import parse




class BossZhiPinSpider(scrapy.Spider):
    name = 'bossspider'
    redis_key = "bossspider:start_urls"
    allowed_domains=['zhipin.com']
    start_urls=['https://www.zhipin.com/c100010000/?ka=sel-city-100010000']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse)


    def parse(self, response):
        #实现翻页

        job_summuys = response.css(".job-list li")

        for job_summuy in job_summuys:
            item = ZhiPinUrlItem()
            jobname=job_summuy.css(".info-primary .job-title::text").extract_first("")
            item["job_name"]=jobname
            post_url=job_summuy.css(".info-primary .name a::attr(href)").extract_first("")
            J_url=parse.urljoin(response.url,post_url)
            item["jobs_url"]=J_url
            yield Request(J_url, meta={"job_url":J_url},callback=self.parse_detail)
            item["company_name"]=job_summuy.css(".info-company .name a::text").extract_first("")
            yield item
        next_url=response.css(".page .next::attr(href)").extract_first("")
        n_url = parse.urljoin(response.url, next_url)
        yield Request(n_url,callback=self.parse)



    #解析详情数据
    def parse_detail(self,response):

        Job_Item = BosszhipinItem()

        company_name =response.css(".info-company .name a::text").extract_first("")
        company_statuses =response.css(".info-company p::text").extract_first("")
        company_address = response.css(".info-primary p::text").extract_first("")
        company_type=response.css(".info-company p a::text").extract_first("")
        company_web=response.css(".info-company p:nth-of-type(2)::text").extract_first("")

        public_data =response.css(".job-author .time::text").extract_first("")
        salary =response.css(".info-primary .badge::text").extract_first("")
        job_name = response.css(".info-primary .name h1::text").extract_first("")
        job_describe =response.css(".detail-content .text::text").extract()

        # #将解析后的数据装入数实体层
        Job_Item["company_name"]=company_name
        Job_Item["company_statuses"]=company_statuses
        Job_Item["company_address"] =company_address
        Job_Item["company_type"] =company_type
        Job_Item["company_web"] =company_web
        Job_Item["public_data"] =public_data
        Job_Item["salary"] =salary
        Job_Item["job_name"] =job_name
        Job_Item["job_describe"] =job_describe

        yield Job_Item



