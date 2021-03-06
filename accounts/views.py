from django.contrib.auth import login, get_user_model, logout
from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q

User=get_user_model()

# def check(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('/notes')
#     else:
#         return HttpResponseRedirect('/register')    

def profile(request):
    context={}
    return render(request,'profiles/profile_page.html',context)


def check(request):
    return render(request,"check.html")



def register(request, *args, **kwargs):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        a=form.cleaned_data.get("email")
        user_obj=User.objects.get(email=a)
        login(request, user_obj)
        return HttpResponseRedirect('/')
    return render(request, 'accounts/register.html', {'form':form})


def user_login(request, *args, **kwargs):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj=form.cleaned_data.get('user_obj')  
        print(user_obj)           
        login(request, user_obj)
        return HttpResponseRedirect('/')
    return render(request, 'accounts/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')