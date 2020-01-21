from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.
class CodeProjects(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    #Randomly generated string
    document = models.TextField(primary_key=True)
    author = models.ForeignKey('Member',on_delete=models.CASCADE)
    
class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.TextField(max_length=25)
    teacher = models.BooleanField(default=False)

    def __str__(self):
        return "{1}, {0}".format(self.user.first_name,self.user.last_name)
    
