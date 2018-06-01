#author --vincent--
import pymongo
import re

class MongoManage(object):
    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1',28017)
        self.db=self.client['booszp']

    def get_one(self):
        return self.db.detail.find_one()

    def get_more(self):
        return self.db.detail.find({})

    def add_one(self):
        '''新增数据'''
        info = self.get_more()
        count=0
        #统一职位名称
        for item in info:
            job_name = item['job_name']
            count +=1
            if re.search('产品经理|产品总监',job_name):
                 rest =self.db.detail.update_one({'_id':item['_id']}, {'$set':{'job_type':'product'}})
                 print(rest)
                 continue
            elif re.search('运营|项目|城市',job_name):
                 rest =self.db.detail.update_one({'_id': item['_id']}, {'$set':{'job_type': 'operation'}})
                 print(rest)
                 continue
            elif re.search('设计|美工', job_name):
                 rest = self.db.detail.update_one({'_id': item['_id']}, {'$set':{'job_type': 'artwork'}})
                 print(rest)
                 continue
            elif re.search('算法|图像|学习|语言', job_name):
                 rest =self.db.detail.update_one({'_id': item['_id']},{'$set':{'job_type': 'algorithm'}} )
                 print(rest)
                 continue
            elif re.search('测试', job_name):
                 rest =self.db.detail.update_one({'_id': item['_id']}, {'$set':{'job_type': 'test'}})
                 print(rest)
                 continue
            elif re.search('开发|工程师|[a-zA-Z]+|运维|架构|技术支持|大数据',job_name):
                 rest =self.db.detail.update_one({'_id': item['_id']},{'$set':{'job_type': 'development'}} )
                 print(rest)
                 continue
            elif re.search('销售',job_name):
                 rest =self.db.detail.update_one({'_id': item['_id']}, {'$set':{'job_type': 'sale'}})
                 print(rest)
                 continue
            else:
                 rest =self.db.detail.update_one({'_id': item['_id']}, {'$set':{'job_type': 'other'}})
                 print(rest)

    #薪资取平均数
    def update(self):
        info = self.get_more()
        pattern =re.compile('\d+')
        for item in info:
            salary =str(item['salary'])
            money=pattern.findall(salary)
            if len(money)==1:
                resu=money[0]
                print(resu)
            else:
                sum=int(money[0])+int(money[1])
                result = int(sum/2)*1000
                rest = self.db.detail.update_one({'_id':item['_id']},{'$set':{'salary':result}})
                print(rest)

if __name__ == '__main__':
    obj = MongoManage()
   # result = obj.get_one()
    #obj.update()
    obj.add_one()
