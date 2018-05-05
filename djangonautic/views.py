'''
Created on Apr 27, 2018

@author: S528358
'''
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
#     return HttpResponse('about')
    return render(request, 'about.html')

def homepage(request):
#     return HttpResponse('home')
    print(request.user)
    username = request.user
    return render(request, 'homepage.html',{'username':username})