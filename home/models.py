from abc import abstractclassmethod
from django.db import models
from django.contrib.auth.models import  User, Group
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from PIL import Image
from django.urls import reverse
from django.dispatch import receiver
from datetime import date
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save

from django.utils.translation import activate
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avatar= models.ImageField(upload_to="static/images/avt/%Y/%m", default='avt.png')
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
    
    
            
    @receiver(post_save, sender=User) #add this
    def create_profile(sender, instance, created, **kwargs):
        print("create_proflie")
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def get_absolute_url(self):
        return reverse('profile', kwargs={"pk": self.pk})
    # @receiver(post_save, sender=User) #add this
    # def save_profile(sender, instance,  **kwargs):
    #     instance.profile.save()
    # post_save.connect(create_profile,sender=User)
        
    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
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
    
    
    def Nu_task(self):
        Nu_task= Task.objects.filter(project=self.id).count()
        return Nu_task
    def Nu_taskDone(self):
        Nu_taskDone=Task.objects.filter(project=self.id).filter(status='Incomplete').count()
        return Nu_taskDone
    def DayLeft(self):
        prj=Project.objects.get(id=self.id)
        dl= prj.deadline
        print('dl:',dl)
        
        day_now= date.today()
        print('day_now:',day_now)
        
        daysLeft= (dl - day_now).days
        print('daysLeft:',daysLeft)
        
        s=''
        if (daysLeft) > 1:
            s= str(daysLeft) + ' days left'
        elif (daysLeft) == 1:
            s= str(daysLeft) + ' day left'
        else:
            s= '0 day'
        return s
    
    @property    
    def __str__(self):
        return self.name_project

    def __str__(self):
        return self.decription
    
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={"pk": self.pk})
    
# ####################################

class Task(ItemBase):
    task= models.CharField(max_length=30)
    project= models.ForeignKey(Project,on_delete=models.SET_NULL, null=True)
    # CASCADE: xóa prj thì task xóa theo
    # SET_NULL
    def __str__(self):
        return self.task
    
# ######################################
from django.db.models import Count
class MyGroup(Group):
    class Meta:
        proxy = True
    def numMember(self):
        return User.objects.filter(groups__name=self.name).count()
    def numProject(self):
        return Project.objects.filter(group__name=self.name).count()
    
# class Membership(models.Model):
#     person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
#     date_joined = models.DateField(auto_now_add=True)