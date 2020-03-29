"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from sample_blog.views import index,charts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', index, name='docs' ),
    path('charts/', charts, name='charts' ),
    path('', index ),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('sample_blog.urls', namespace='data')),  # 引入app的urls.py，给个命名空间
#     #re_path('test/$', index, name='docs' ),   # 不在app中建urlpatterns也可以实现给网页命名
#     path('test/', index, name='docs' ),   # 这句可以代替上面那句，这句更简单；
# ]
