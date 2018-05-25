from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('accounts:profile_page',slug=user)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html',{'form':form})

def login_view(request, slug=None):
   
#     print(request.GET.urlencode())
    if request.method == 'POST':
        print('login user',slug)
        print('login_view',request.user)
        print(request.POST)
        print('username' in request.POST)
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))            
            else:
                return redirect('accounts:profile_page',slug=user)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):    
    logout(request)
    return redirect('accounts:login_view')

@login_required(login_url='/accounts/login')
def article_delete(request, slug=None):
    print(slug)
    user = request.user
    print('user delete',user)
    obj = Article.objects.get(slug=slug,authorid=user)
    print('delete',obj.slug)
    obj.delete()
    return redirect('accounts:profile_page',slug=user)

@login_required(login_url='/accounts/login')
def profile_page(request,slug=None):
    print('calling profil page',request.method)
    print('logged in as',request.user)
    print('slug is',slug)
    obj = Article.objects.all()
    users = User.objects.all()    
    ans = []
    for i in obj:
        if str(i.authorid) == str(slug):
            ans.append(i)
    context = {
        'obj':obj,
        'ans':ans,
        }
    for i in users:
        print(i)
#     print(request.user in users)
    print(ans)
<<<<<<< HEAD
#     print(ans[0].authorid)
=======
#    print(ans[0].authorid)
>>>>>>> c2e8fd3afb69f93cbc780cf1256974a8a3ac4825
    if str(request.user) == str(slug):
        return render(request, 'accounts/profile.html', {'ans':ans})
    else:
        return render(request, 'accounts/guest_profile.html', {'ans':ans})
