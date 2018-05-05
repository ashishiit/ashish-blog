'''
Created on Apr 29, 2018

@author: S528358
'''
from django.urls import path, re_path
from . import views as core_views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [    
   path('sign_up',core_views.sign_up, name = 'sign_up'),
   #path('login',views.login_view, name = 'login_view'),
   path('login',core_views.login_view, name='login_view'),
#    path('logout', views.logout, name = 'logout_view'),
   path('logout',auth_views.logout,{'next_page': '/accounts/login'}, name='logout_view'),
#     path('profile', core_views.profile_page, name ='profile_page'),
    re_path(r'^(?P<slug>[\w-]+)/$', core_views.profile_page, name = 'profile_page'),
]