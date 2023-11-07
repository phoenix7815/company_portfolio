from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from info.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.

def logi(request):
    if request.method=="POST":
        username=request.POST['username']
        request.session['username']=username
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print("hello")
        if user is not None:
            return redirect('info')
    else:
        print(request) 
        form=companyLoginform()
    return render(request,'login.html',{'form':form})


def register(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        form = companyRegisterform(request.POST)
        if(form.is_valid()):
            form.save()
            request.session['username']=username
            username = form.cleaned_data.get('username')
            return redirect('companydetails')

    else:
        form=companyRegisterform()
    return render(request,'register.html',{'form':form})
    
def companydetails(request):
    if(request.method=="POST"):
        form=vacant_positio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')

    else:
        username=request.session['username']
        print(username)
        form=vacant_positio(initial={'username':username})
        
    return render(request,'details.html',{'form':form})


def companyinfo(request):
    username=request.session['username']
    print(username,"$$")
    pos=vacant_position.objects.get(username=username)
    users=pos.user_details_set.all()
    return render(request,'companyinfo.html',{'pos':pos,'users':users})

def about(request,username):
    detail=user_details.objects.get(username=username)
    return render(request,'about.html',{'detail':detail})