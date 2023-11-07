from django.shortcuts import render,redirect
from .models import vacant_position,user_details
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.urls import reverse

# Create your views here.

@login_required
def home(request):
    username=request.user.username
    userdetails=(user_details.objects.filter(username=username))
    return render(request,'home.html',{'userdetails':userdetails})

# @method_decorator(login_required, name='dispatch')
@login_required
def company_details(request):
    username=request.user
    temp_list=user_details.objects.get(username=username)
    apply_no=temp_list.application.all()
    print(apply_no)
    vacant_position_list=vacant_position.objects.all()
    vacant_position_list=vacant_position_list.exclude(username__in=apply_no.values_list('username',flat=True))
    skil=position.objects.all()
    return render(request,'info/vacant_position_list.html',{"vacant_position_list":vacant_position_list,"skill":skil})

@login_required
def particular(request,username):
    usernam=request.user
    details=vacant_position.objects.get(username=username)
    user=user_details.objects.get(username=usernam)
    skill_user=user.known_skills.all()
    skills_req=position.objects.get(position_name=details.role)
    skills_req=skills_req.reqd_skill.all()
    skills_missing=skills_req.exclude(skill_name__in=skill_user.values_list('skill_name',flat=True))
    return render(request,'info/particular.html',{'details':details,'skills_reqd':skills_req,'skills_missing':skills_missing})


def signup(request):
    return render(request,"signup.html")

def register(request):
    register_user=reverse('registeruser')
    if request.method == 'POST':
        usernam=request.POST.get('username')
        
        print("Register post")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            request.session['username']=usernam
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('extradetails')
    else:
        form = UserRegisterForm()
    return render(request, 'info/register.html', {'form': form, 'title':'register here' ,'register_user':register_user})


def extradetails(request):
    if request.method=='POST':
        form=extra_details(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('known_skills')
            print(email)
            return redirect('login')
    else:
        username=request.session['username']
        form =extra_details(initial={'username':username})
    return render(request,'info/extradetails.html',{'form':form})


def apply(request,primary_key):
    print("hii")
    if request.method=='GET':
        username=request.user
        record=user_details(username=username)
        new_position=vacant_position(username=primary_key)
        record.application.add(new_position)
        print("hiii")
    return redirect('details')

    
