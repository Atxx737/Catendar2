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
    list_display=('task','status','deadline','project')

# @admin.register(ToDo)
# class todoAdmin(admin.ModelAdmin):
#     list_display=('project','task','todo_CHOICES',)

admin.site.register(Profile)

