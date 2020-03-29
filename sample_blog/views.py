from django.shortcuts import render
from sample_blog.models import PostInfo    # 导入已写好的数据结构
from django.core.paginator import Paginator  # 导入分页器

# Create your views here.


def index(request):
    limit = 10  # 每页展示几条帖子
    all_post_info = PostInfo.objects[:300]  # 取前300个帖子的数据，取所有86850条数据会很慢
    paginatior = Paginator(all_post_info, limit)   # 用分页器分页
    page_num = request.GET.get('page', 1)  # 取request中的页码，取不到就为1
    # print('request:',request)
    # print('request.GET:',request.GET)
    loaded = paginatior.page(page_num)  # 取page_num那一页的数据，一般是10条
    docs_num = PostInfo.objects.count()   # 通过此函数得知共有86850条数据
    add_num = 7742      # 找出发帖量最多的一天，当天发帖数作为此参数

    context = {
        'one_page_post': loaded,   # 每页更新的帖子信息
        'docs_num': docs_num,
        'add_num': add_num,
    }
    return render(request, 'new_index.html',context)

# 各品类发帖总量柱状图，生成所需数据
def total_post():
    pipeline = [
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
    ]

    for i in PostInfo._get_collection().aggregate(pipeline):
        #print(i)
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data
series_post = [i for i in total_post()]

# pie1:一天内成交物品种类分布图，所需数据：
def one_day_deal_cate():
    pipeline = [
        {'$match':{'time':1}},
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
        {'$sort':{'counts':1}}
    ]

    for i in PostInfo._get_collection().aggregate(pipeline):
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data
pie1_data = [i for i in one_day_deal_cate()]

# pie2:一天内成交物品地区分布图，所需数据：
def one_day_deal_area():
    pipeline = [
        {'$match': {'time': 1}},
        {'$group': {'_id': {'$slice': ['$area', 1]}, 'counts': {'$sum': 1}}},
        {'$sort': {'counts': 1}}
    ]

    for i in PostInfo._get_collection().aggregate(pipeline):
        data = {
            'name':i['_id'][0] if i['_id'] else '缺失',
            'y':i['counts']
        }
        yield data
pie2_data = [i for i in one_day_deal_area()]

# 某地区热销类目top3
def cates_top3(area):
    top3_list = []
    pipeline = [
        {'$match': {'area': {'$all': [area]}}},
        {'$group': {'_id': {'$slice': ['$cates', 2, 1]}, 'counts': {'$sum': 1}}},
        {'$sort': {'counts': -1}},
        {'$limit': 3}
    ]
    for i in PostInfo._get_collection().aggregate(pipeline):
        data = {
            'name': i['_id'][0],
            'y': i['counts']
        }
        top3_list.append(data)
    return(top3_list)



def charts(request):
    context = {
        # 'chart_CY':series_CY,
        # 'chart_TZ':series_TZ,
        # 'chart_HD':series_HD,
        'chaoyang_top3':cates_top3('朝阳'),
        'haidian_top3': cates_top3('海淀'),
        'tongzhou_top3': cates_top3('通州'),
        'series_post':series_post,
        'pie1_data':pie1_data,
        'pie2_data':pie2_data,
    }
    return render(request,'charts.html',context)