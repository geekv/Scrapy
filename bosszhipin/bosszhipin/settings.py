# -*- coding: utf-8 -*-
# author：--Vincent--
# Scrapy settings for bosszhipin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'bosszhipin'

SPIDER_MODULES = ['bosszhipin.spiders']
NEWSPIDER_MODULE = 'bosszhipin.spiders'

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"

REDIRECT_ENABLED = False
RETRY_TIMES = 1
DOWNLOAD_TIMEOUT = 10 #下载超时时间


#
# MONGO_URL = 'mongodb://127.0.0.1:27017/'
# MONGO_DATABASE = 'bosszp'

MONGODB_HOST='127.0.0.1'
MONGODB_PORT=27017
MONGODB_DBNAME='booszhipin'
MONGODB_DOCNAME1='summary'
MONGODB_DOCNAME2='detail'

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
SCHEDULER_PERSIST = True
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


# 种子队列的信息
REDIS_URL = None
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379#6379
FILTER_URL = None
FILTER_HOST = '127.0.0.1'
FILTER_PORT = 6379#6379
FILTER_DB = 0


ITEM_PIPELINES = {
    'bosszhipin.pipelines.BosszhipinPipeline':320,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bosszhipin (+http://www.yourdomain.com)'

#随机生产下载时间
#delay_time=[random.random()for i in range(5)]




# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'bosszhipin.middlewares.BosszhipinSpiderMiddleware': 543,
#
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'bosszhipin.middlewares.MyCustomDownloaderMiddleware': 543,
    'bosszhipin.middlewares.UserAgentMiddleware':543,
    # 'bosszhipin.middlewares.ProxyMiddleware':543,

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bosszhipin.pipelines.BosszhipinPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
