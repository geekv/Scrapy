# author：--Vincent--
from scrapy_redis.spiders import RedisSpider

from scrapy.http import Request
from bosszhipin.items import ZhiPinUrlItem,BosszhipinItem,BossJobItemLoader
from urllib import parse




class BossZhiPinSpider(RedisSpider):
    name = 'bossspider'
    redis_key = "bossspider:start_urls"
    allowed_domains=['zhipin.com']
    start_urls=['https://www.zhipin.com/c100010000/?ka=sel-city-100010000']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        # do stuff交给scrapy下载并进行解析

        #解析列表页的所有职位url

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



    def parse_detail(self,response):


        # Job_Item = BosszhipinItem()
        # company_name =response.css(".info-company .name a::text").extract_first("")
        # company_statuses =response.css(".info-company p::text").extract_first("")
        # company_address = response.css(".info-primary p::text").extract_first("")
        # company_type=response.css(".info-company p a::text").extract_first("")
        # company_web=response.css(".info-company p:nth-of-type(2)::text").extract_first("")
        #
        # public_data =response.css(".job-author .time::text").extract_first("")
        # salary =response.css(".info-primary .badge::text").extract_first("")
        # job_name = response.css(".info-primary .name h1::text").extract_first("")
        # job_describe =response.css(".detail-content .text::text").extract()
        #
        # Job_Item["company_name"]=company_name
        # Job_Item["company_statuses"]=company_statuses
        # Job_Item["company_address"] =company_address
        # Job_Item["company_type"] =company_type
        # Job_Item["company_web"] =company_web
        # Job_Item["public_data"] =public_data
        # Job_Item["salary"] =salary
        # Job_Item["job_name"] =job_name
        # Job_Item["job_describe"] =job_describe
        #
        # yield Job_Item

        # 使用Item_loard 进行对象添加，解析页面，提取字段

        item_loader = BossJobItemLoader(item=BosszhipinItem(),response=response)
        item_loader.add_css("company_name", ".info-company .name a::text")
        item_loader.add_css("company_statuses", ".info-company p::text")
        item_loader.add_css("company_address", ".info-primary p::text")
        item_loader.add_css("company_type", ".info-company p a::text")
        item_loader.add_css("company_web", ".info-company p:nth-of-type(2)::text")
        item_loader.add_css("public_data", ".job-author .time::text")
        item_loader.add_css("salary", ".info-primary .badge::text")
        item_loader.add_css("job_name", ".info-primary .name h1::text")
        item_loader.add_css("job_describe", ".detail-content .text::text")

        job_item = item_loader.load_item()
        yield job_item
