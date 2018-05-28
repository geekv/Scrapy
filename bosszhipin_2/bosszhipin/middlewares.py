# author：--Vincent--
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
import logging
from .cookie import iniCookie,updateCookie,removeCookie
from scrapy import signals
from .user_agents_pc import agents
import random
from scrapy.downloadermiddlewares.retry import RetryMiddleware
import redis
import json
from scrapy.utils.response import response_status_message
import pdb
from scrapy.exceptions import IgnoreRequest
import base64

class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent

logger=logging.getLogger(__name__)

class BosszhipinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class CookiesMiddleware(RetryMiddleware):

    def __init__(self, settings, crawler):
        RetryMiddleware.__init__(self, settings)
        self.rconn = settings.get("RCONN", redis.Redis(crawler.settings.get('REDIS_HOST', 'localhsot'), crawler.settings.get('REDIS_PORT', 6379)))
        iniCookie(self.rconn, crawler.spider.name)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings, crawler)

    def process_request(self, request, spider):
        redisKeys = self.rconn.keys()
        while len(redisKeys) > 0:
            elem = random.choice(redisKeys)
            # pdb.set_trace()
            if b'bossspider:Cookies' in elem:
                # pdb.set_trace()
                elem = str(elem, 'utf-8')
                cookie = json.loads(str(self.rconn.get(elem), 'utf-8'))
                request.cookies = cookie
                request.meta["accountText"] = elem.split("Cookies:")[-1]
                break
            else:
                redisKeys.remove(elem)

    def process_response(self, request, response, spider):
        reason = response_status_message(response.status)
        if response.status in [300, 301, 302, 303]:
           #pdb.set_trace()
            if reason == '301 Moved Permanently':
                return self._retry(request, reason, spider) or response  # 重试
            else:
                raise IgnoreRequest
        elif response.status in [403, 414]:
            logger.error("%s! Stopping..." % response.status)
            os.system("pause")
            updateCookie(request.meta['accountText'], self.rconn, spider.name, request.cookies)
            return self._retry(request, reason, spider) or response  # 重试
        else:
            return response


# 代理服务器
proxyServer = "http://http-cla.abuyun.com:9030"

#H1H05M2445P7666C:BF0788D90B92786D
#H4T0V56651C9828C:BF0788D90B92786D
# 代理隧道验证信息
proxyUser = "H2C6M19J93T7722C"
proxyPass = "4B4CA62A01EC541F"


# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer

        request.headers["Proxy-Authorization"] = proxyAuth
