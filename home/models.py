from abc import abstractclassmethod
from django.db import models
from django.contrib.auth.models import  User, Group
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from PIL import Image
from django.urls import reverse
from django.db.models.fields.related import ForeignKey

from django.utils.translation import activate
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to="static/images/avt/%Y/%m", default='static/images/avt.png')
    birth= models.DateField(blank=True,null=True)
    gender_CHOICES=(
        ('Female','Female'),
        ('Male','Male '),
        ('Other','Other ')
    )
    gender=models.CharField(max_length=15, choices=gender_CHOICES, default='Male')
    bio=models.TextField()
    lastname=models.CharField(max_length=30,default='')
    firstname=models.CharField(max_length=30,default='')
    online= models.BooleanField(default=True)
    active= models.BooleanField(default=True)
    
    def __str__(self):
        return f' Profile {self.user.username} '
    
    def save(self):
        super().save()
        avt= Image.open(self.avatar.path)
        if avt.height>300 or avt.width >300:
            output_size= (300,300)
            avt.thumbnail(output_size)
            avt.save(self.avatar.path)
# ######################################

class ItemBase(models.Model):
    decription=models.CharField(default=' ', max_length=100)
    deadline=models.DateField(blank=True,null=True)
    status_CHOICES=(
        ('Complete','Complete'),
        ('Incomplete','Incomplete ')
    )
    status=models.CharField(max_length=15, choices=status_CHOICES, default='Incomplete')
    created_date=models.DateTimeField(auto_now_add=True, null=True)
    updated_date=models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)
    class Meta:
        abstract = True
# ######################################
class Project(ItemBase):
    name_project=models.CharField(max_length=20, unique=True)
    num_task= models.IntegerField(blank=True,null=True)
    num_taskDone=models.IntegerField(blank=True,null=True, default='0')
    group= ForeignKey(Group, on_delete=models.SET_NULL, null= True)
    
    def percent(self):
        a= self.num_taskDone
        b= self.num_task
        return (a/b)*100
    
    @property    
    def __str__(self):
        return self.name_project

    def __str__(self):
        return self.decription
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})
    
# ####################################

class Task(ItemBase):
    task= models.CharField(max_length=30)
    project= models.ForeignKey(Project,on_delete=models.SET_NULL, null=True)
    # CASCADE: xóa prj thì task xóa theo
    # SET_NULL
    def __str__(self):
        return self.task


# ######################################

