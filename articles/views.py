from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
@login_required(login_url='/accounts/login')
def article_list(request):
#     print (request.user)
    obj = Article.objects.all().order_by('time')
    return render(request, 'articles/article_list.html', {'obj':obj})

def article_delete(request,slug=None):
    print(slug)
#     return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    user = article.authorid
    article.delete()    
    return redirect(request, 'accounts:profile_page', slug=user)

@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.authorid = request.user
            instance.save()
            print('Logged in user',instance.authorid)
            return redirect('accounts:profile_page', slug=instance.authorid)
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html', {'form':form})
    
    
