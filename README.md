# Scrapy-Redis<br>
使用Scrapy框架爬取Boss直聘网站的相关信息<br>

环境：<br>
  python（3.6.4） <br>
  redis (2.10.6)  <br>
  Scrapy (1.4.0)  <br>
  Scrapy-Redis(0.7.0) <br>
  Mongodb（3.6.3） <br>

#bosszhipin_version_1 <br>
  简单的做了页面解析功能 <br>
  <br>
#bosszhipin_2  <br>
  封装Item_load、模拟登陆功能 <br>
  <br>
  
  ##创建镜像文件Dockerfile<br>
  
FROM ubuntu<br>
RUN apt-get update<br>
RUN apt-get install -y vim<br>
RUN apt-get -y dist-upgrade openssh-server<br>
RUN apt-get install -y redis-server<br>
RUN apt-get install -y python3.5 python3-pip<br>
RUN apt-get install -y zlib1g zlib1g-dev libffi-dev libssl-dev<br>
RUN apt-get install -y libxml2-dev libxslt1-dev<br>
ADD ./bosszhipin/ /code/<br>
WORKDIR /code/<br>
EXPOSE 3679<br>
RUN ls<br>
RUN pip3 install -r requirements.txt<br>
