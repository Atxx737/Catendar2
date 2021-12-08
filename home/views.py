from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from home.form import  *
from django.contrib import messages 
from home.models import  Project
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import online_users.models
from datetime import timedelta
from django.core.paginator import Paginator
# ######################################

def home_view(request, user_id):
    gr= Group.objects.filter(user=user_id)
    q_project= Project.objects.filter(group__in=gr).filter(status="Incomplete").order_by('-deadline')
    q_prjDone= Project.objects.filter(group__in=gr).filter(status="Complete")
    q_prjTotal= Project.objects.filter(group__in=gr).order_by('deadline')
    #set up pagination
    p_total= Paginator(q_prjTotal,6)
    page_total= request.GET.get('page')
    prjTotal=p_total.get_page(page_total)
    ##############
    p_done= Paginator(q_prjDone,6)
    page_done= request.GET.get('page')
    prjDone=p_done.get_page(page_done)
    ##############
    p_project= Paginator(q_project,6)
    page_project= request.GET.get('page')
    prj=p_project.get_page(page_project)
    
    context={
        "Project":prj,
        "ProjectDone":prjDone,
        "ProjectTotal":prjTotal,
    }
    return render(request,'home.html',context)

def login_view(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home', user.id)
       
    return render(request, 'user/login.html')

def pomodoro_view(request):
    return render(request,'pomodoro.html')

def register_view(request):
    form_signup = RegistrationForm
    if request.method =='POST':
        form_signup = RegistrationForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            messages.success(request, "Sign up Success!")
            url = reverse('login')
            return HttpResponseRedirect(url)
    context={
        'form': form_signup,
    }
    return render(request, 'user/register.html',context )
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def profile_view(request,username):
    user=User.objects.get(username=username)
    profile= Profile.objects.get(user=user.id)
    context={
        'profile':profile
    }
    print(profile)
    return render(request, 'user/profile.html',context)

def editProfile(request,username):
    user=User.objects.get(username=username)
    porfile= Profile.objects.get(user=user.id)
    form= editProfileForm(instance=porfile)
    userForm=UserUpdateForm(instance=user)
    
    if request.method=='POST':
        form= editProfileForm(request.POST,request.FILES,instance=porfile)
        userForm=UserUpdateForm(request.POST,instance=user)
        if form.is_valid() and userForm.is_valid() :
            form.save()
            userForm.save()
            return redirect('profile', username=user.username)
        
    context={
            'form':form,
            'userForm':userForm,
    }
    return render(request,'user/editProfile.html',context)

def createProfile(request,username):
    createProflie=editProfileForm()
    
    if request.method=='POST':
        createProflie=editProfileForm(request.POST)
        if createProflie.is_valid():
            createProflie.save()
            messages.success(request, "Success")
            url = reverse('home', request.user.id)
            return HttpResponseRedirect(url)
        else:
            messages.error(request, "Error create profile")
    
    context={'createProflie':createProflie}
    return render(request,'user/createProfile.html',context)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def createProject_view(request, username):
    form_prj=createProjectForm()
    if request.method=='POST':
        form_prj=createProjectForm(request.POST)
        if form_prj.is_valid():
            form_prj.save()
            messages.success(request, "Success")
            url = reverse('home', request.user.id)
            return HttpResponseRedirect(url)
        else:
            messages.error(request, "Error create project")
    
    context={'form_prj':form_prj}
    return render(request,'project/createProject.html',context)

def updateProject(request,id):
    project= Project.objects.get(id=id)
    form= updateProjectForm(instance=project)
    if request.method=='POST':
        form= updateProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('home',request.user.id)
    context={'form':form}
    return render(request,'project/projectUpdate.html',context)

def deleteProject(request, id):
    project= Project.objects.get(id=id)
    if request.method=='POST':
        project.delete()
        return redirect('home',request.user.id)
        
    context={'project':project}
    return render(request,'project/confirm-delete.html',context)
    
def detailProject(request,project_id):
    prj= Project.objects.get(id=project_id)
    task_obj= Task.objects.filter(project=prj.id)
    gr= Group.objects.get(name=prj.group)
    member=[]
    for i in User.objects.filter(groups__name=gr.name):
        member.append(i.username)
        
    #set up pagination
    p_task= Paginator(task_obj,4)
    page_task= request.GET.get('page')
    task=p_task.get_page(page_task)
    context={
        'project':prj,
        'task':task,
        'member':member,
    }
    return render(request,'project/projectDetail.html',context)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def createTask(request,project_id):
    prj= Project.objects.get(id=project_id)
    formTask=createTaskForm(initial={'project':prj})
    
    if request.method=='POST':
        formTask=createTaskForm(request.POST)
        if formTask.is_valid():
            formTask.save()
            messages.success(request, "Success")
            return redirect('detail',project_id=prj.id)
        else:
            messages.error(request, "Error create task")
        
    context={
        'formTask':formTask,
    }
    return render(request,'task/createTask.html', context)

def updateTask(request,task_id):
    tsk=Task.objects.get(id=task_id)
    prj= Project.objects.get(task=tsk)
    form_updateTask= updateTaskForm(instance=tsk)
    if request.method=='POST':
        form_updateTask= updateTaskForm(request.POST,instance=tsk)
        if form_updateTask.is_valid():
            form_updateTask.save()
            return redirect('detail',prj.id)
        
    context={
        'form_updateTask':form_updateTask,
    }
    return  render(request,'task/updateTask.html',context)

def deleteTask(request, id):
    tskDelete=Task.objects.get(id=id)
    if request.method=='POST':
        tskDelete.delete()
        return redirect('home',request.user.id)
    
    context={'tskDelete':tskDelete}
    return render(request,'task/deleteTask.html',context)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createGroup(request, user_id):
    member= User.objects.get(id=user_id)
    if request.method=='POST':
        name=request.POST.get('name')
        if name != '':
            group=Group.objects.get_or_create(name = name)
            group = Group.objects.get(name = name)
            member.groups.add(group)
            group.save()
   
    return redirect('group',user_id)

def group_view(request,user_id):
    gr= MyGroup.objects.filter(user=user_id)
    context={
        'gr':gr,
    }
    return render(request,'user/group/group.html',context)

def deleteGroup(request,group_id):
    grDelete=Group.objects.get(id=group_id)
    if request.method=='POST':
        grDelete.delete()
        return redirect('group',request.user.id)
    context={
        'grDelete':grDelete
    }
    return render(request,'user/group/deleteGroup.html',context)

def addUser_toGroup(request, group_id):
    if request.method=='POST':
        userName=request.POST.get('userName')
        g = Group.objects.get(id=group_id)
        users = User.objects.get(username=userName)
        # g.user_set.add(users)
        users.groups.add(g)
    return redirect('detailGroup',group_id)

def detailGroup(request,group_id):
    gr= Group.objects.get(id=group_id)
    member=[]
    for i in User.objects.filter(groups__name=gr.name):
        member.append(i.username)
    project=[]
    for i in Project.objects.filter(group__name=gr.name):
        project.append(i.name_project)
        
    user= User.objects.all()
    context={
        'gr':gr,
        'member':member,
        'project':project,
        'group_id':group_id,
        'user':user,
    }
    return render(request,'user/group/groupDetail.html',context)
    
# ######################################

