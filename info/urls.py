from django.urls import path,include
from . import views
urlpatterns=[
     path('company',views.company_details,name="details"),
     path('company/<str:username>',views.particular,name="particular"),
    path('',views.home,name="home"),
     path('', include('django.contrib.auth.urls')),
    path('register',views.register,name="registeruser"),
    path('extadetails',views.extradetails,name="extradetails"),
   path('apply/<str:primary_key>',views.apply,name='apply'),  
   path('', include('django.contrib.auth.urls')),
]