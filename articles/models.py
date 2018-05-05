from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    slug = models.SlugField()
    time = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(null=True, blank=True)
    
    authorid = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)
    
    
    
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:30]+'...'
    
    def get_absolute_url(self):
        return '/accounts/%s' %self.authorid
    