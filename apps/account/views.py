from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.


def login_view(request):
    if request.method=='GET':
        next=request.GET.get('next')
        return render(request,'login.html',{'next':next})
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        next=request.GET.get('next')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            next=next if next else '/'
            return redirect(next)
        else:
            return render(request,'login.html',{'next':next})

def logout_view(request):
    logout(request)
    return redirect('/')