'''
Created on Apr 28, 2018

@author: S528358
'''
from django.urls import path, re_path
from . import views
app_name = 'articles'
urlpatterns = [
    
   
    path('', views.article_list, name = 'article_list'),
    path('create',views.article_create, name = 'article_create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name = 'article_detail'),
]
