from django.shortcuts import render,redirect
from .forms import *
from .models import vacant_position,user_details
from django.views import generic
from django.contrib.auth import login


# Create your views here.

def home(request):
    username=request.user.username
    userdetails=(user_details.objects.all())
    return render(request,'home.html',{'userdetails':userdetails})


class company_details(generic.ListView):
    model=vacant_position

    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # You can customize the redirection URL

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})