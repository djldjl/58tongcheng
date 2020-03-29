# 58tongcheng
用django搭的，展示58同城的数据，两个页面，一个是所有商品的信息，一个是几个统计图表；
mysite是Django项目名称，目录里面的urls.py有改写的内容；
sample_blog是APP的名称，目录里面的models.py、views.py有改写的内容；
static目录下是依赖的css\js\img等静态资源，semantic\highcharts依赖的资源都在其中；
template目录是网页模板，就用了3个html:base.html、charts.html、new_index.html；
manage.py和db.sqlite3是建Django项目和数据库时自动生成的。
用的mongo数据库，读取其中的数据；没用自带的sqlite.
