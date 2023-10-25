from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Company(models.Model):
    company_name=models.CharField(primary_key=True,max_length=100,help_text="Enter Company Name")
    Description=models.TextField(max_length=200,help_text="Enter About the Company",null=True)
    def __str__(self):
        return self.company_name

class skills(models.Model):
    skill_name=models.CharField(max_length=100)
    def __str__(self):
        return self.skill_name
    
class position(models.Model):
    position_name=models.CharField(primary_key=True,max_length=100)
    reqd_skill=models.ManyToManyField(skills)
    def __str__(self):
        return self.position_name

class vacant_position(models.Model):
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)
    role=models.ForeignKey(position,on_delete=models.CASCADE,help_text="Select position for the company")
    role_description=models.TextField(max_length=400,help_text="Enter description about Role..",null=True)
    exp=models.IntegerField(default=0)
    def __str__(self):
        return str(self.company_name)
   
class user_details(models.Model):
    username=models.CharField(max_length=100,primary_key=True,default="")
    name=models.CharField(max_length=100,help_text="Enter your name")
    age=models.IntegerField(help_text="Enter your age")
    known_skills=models.ManyToManyField(skills,help_text="Choose your skiils")
    role=models.ManyToManyField(position)
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    pass