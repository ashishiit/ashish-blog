from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    time = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(null=True, blank=True)    
    authorid = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)   
    
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:30]+'...'
    
    def get_absolute_url(self):
        return '/accounts/%s' %self.authorid

def create_slug(instance, new_slug=None):
        slug = slugify(instance.title)
        if new_slug is not None:
            slug = new_slug
        qs = Article.objects.filter(slug=slug)
        exists = qs.exists()
        if exists:
            new_slug = "%s-%s" %(slug, qs.first().id)
            return create_slug(instance, new_slug=new_slug)
        return slug
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    
pre_save.connect(pre_save_post_receiver, sender=Article)