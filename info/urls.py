from django.urls import path,include

from . import views
urlpatterns=[
     path('company',views.company_details.as_view(),name="details"),
    path('',views.home,name="home"),
    path('register',views.register,name="registeruser"),
    path('extadetails',views.extradetails,name="extradetails"),
   path('apply/<int:primary_key>',views.apply,name='apply'),  
]