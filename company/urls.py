from django.urls import path,include
from . import views
urlpatterns=[
     path('',views.register,name="companyregister"),
     path('details',views.companydetails,name="companydetails"),
     path('info',views.companyinfo,name="info"),
     path('login',views.logi,name='logincompany'),
     path('about/<str:username>',views.about,name='about')
]