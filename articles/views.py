from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify
from articles.forms import CreateArticle
# Create your views here.
@login_required(login_url='/accounts/login')
def article_list(request):
    obj = Article.objects.all().order_by('time')
    return render(request, 'articles/article_list.html', {'obj':obj})

def article_delete(request,slug=None):
    article = Article.objects.get(slug=slug)
    user = article.authorid
    article.delete()    
    return redirect(request, 'accounts:profile_page', slug=user)

@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST or None,request.FILES or None)
        if form.is_valid():            
            instance = form.save(commit=False)
            print('slug present ?',instance.slug)
            instance.authorid = request.user
            instance.slug = slugify(instance.slug)
            print('slug=',instance.slug)
            instance.save()
            print('Logged in user',instance.authorid)
            return redirect('accounts:profile_page', slug=instance.authorid)
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html', {'form':form})
    
    
def article_update(request,slug=None):
    instance = Article.objects.get(slug=slug)
    print(instance.title)
    form = forms.CreateArticle(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('accounts:profile_page', slug=instance.authorid)
    context = {
        'title':instance.title,
        'instance':instance,
        'form':form,
        }
    return render(request,'articles/article_create.html', {'form':form})

def article_detail(request,slug=None):
    print('detail slug',slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})