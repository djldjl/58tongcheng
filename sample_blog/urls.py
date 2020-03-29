from django.urls import path,include,re_path
from . import views

app_name = 'sample_blog'

urlpatterns = [
    re_path('^$', views.index),
    re_path('docs/$', views.index, name='docs' ),
    re_path('charts/$', views.charts, name='charts' ),
]