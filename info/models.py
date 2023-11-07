from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
    
    username=models.CharField(max_length=100,primary_key=True)
    company_name=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    company_description=models.TextField(max_length=2000,help_text="Enter Description about Company",null=True)
    role=models.ForeignKey(position,on_delete=models.CASCADE,help_text="Select position for the company")
    role_description=models.TextField(max_length=2000,help_text="Enter description about Role..",null=True)
    exp=models.IntegerField(default=0)
    workplace=models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.company_name)
   
class user_details(models.Model):
    username=models.CharField(max_length=100,primary_key=True,default="")
    first_name=models.CharField(max_length=100,help_text="Enter your first name", null=True)
    last_name=models.CharField(max_length=100,help_text="Enter your first name",null=True)
    age=models.IntegerField(help_text="Enter your age",null=True)
    known_skills=models.ManyToManyField(skills,help_text="Choose your skiils")
    role=models.ManyToManyField(position)
    email=models.EmailField(null=True)
    phone_no=models.BigIntegerField(null=True)
    description=models.TextField(help_text="Enter about you",null=True)
    application=models.ManyToManyField(vacant_position,help_text="Applied Companies")
    def __str__(self):
        return str(self.first_name)