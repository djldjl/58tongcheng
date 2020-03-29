from django.db import models
from mongoengine import *
from mongoengine import connect
connect('ganji', host='127.0.0.1', port=27017)   # 连接ganji数据库


# Create your models here.

# 创建帖子信息类，继承自mongoengine的文件类
class PostInfo(Document):
    area = ListField(StringField())
    title = StringField()
    cates = ListField(StringField())
    price = StringField()

    pub_date = StringField()      # 数据集里面所有的字段都要有，就算不用也得列出来
    url = StringField()
    look = StringField()
    time = IntField()
    cates2 = StringField()

    meta = {'collection':'goods_info'}   # 定位好是goods_info数据集

# for i in PostInfo.objects[:100]:     #测试mongodb是否连接成功
#     print(i.title,i.area,i.cates,i.price)

# 找出发帖量最大的10天
# pipeline = [
#     {'$group': {'_id':'$pub_date','counts':{'$sum':1}}},
#     {'$sort': {'counts': -1}},
#     {'$limit': 10}
# ]
#
# for i in PostInfo._get_collection().aggregate(pipeline):
#     print(i)















