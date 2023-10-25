from django.urls import path,include
from . import views
urlpatterns=[
     path('company',views.company_details.as_view(),name="details"),
    path('',views.home),
    path('signup',views.signup)

]