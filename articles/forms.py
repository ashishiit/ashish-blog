'''
Created on May 3, 2018

@author: S528358
'''
from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body','pic']