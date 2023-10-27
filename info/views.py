from django.shortcuts import render,redirect
from .models import vacant_position,user_details
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *

# Create your views here.

@login_required
def home(request):
    username=request.user.username
    userdetails=(user_details.objects.filter(username=username))
    return render(request,'home.html',{'userdetails':userdetails})

@method_decorator(login_required, name='dispatch')
class company_details(generic.ListView):
    model=vacant_position

def signup(request):
    return render(request,"signup.html")


def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        print("Register post")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            request.session['username']=username
            form.save()
            username = form.cleaned_data.get('username')
            
            
            return redirect('extradetails')
    else:
        form = UserRegisterForm()
    return render(request, 'info/register.html', {'form': form, 'title':'register here'})


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
    if request.method=='GET':
        username=request.user
        record=user_details(username=username)
        new_position=vacant_position(id=primary_key)
        record.application.add(new_position)
    return redirect('details')