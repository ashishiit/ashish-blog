from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Article
# Create your views here.
def sign_up(request):
#     print(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
#             print(user)
            return redirect('accounts:profile_page', slug=user)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:profile_page', slug=user)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):    
    logout(request)
    return redirect('accounts:login_view')

def profile_page(request,slug=None):
#     print(slug)
#     print(request.user.get_username())
    obj = Article.objects.all()
    ans = []
    for i in obj:
        if i.authorid == request.user:
            ans.append(i)
        
    return render(request, 'accounts/profile.html', {'ans':ans})
    