from django.contrib import admin
from home.models import *

# admin.site.register(Project)

# Register your models here.
@admin.register(Project)
class projectAdmin(admin.ModelAdmin):   
    list_display= ('id','name_project','decription',
                   'deadline','group',
                   'status','created_date')
    list_filter= ('status','name_project', 'group')

@admin.register(Task)
class taskAdmin(admin.ModelAdmin):
    list_display=('id','task','status','deadline','project')
    list_filter= ('status','project')
# @admin.register(ToDo)
# class todoAdmin(admin.ModelAdmin):
#     list_display=('project','task','todo_CHOICES',)

@admin.register(Notificatiion)
class notificationAdmin(admin.ModelAdmin):
    list_display=('notification_type','from_user','to_user')
    list_filter= ('notification_type','from_user','to_user')
    
admin.site.register(Profile)
