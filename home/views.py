from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from home.form import  *
from django.contrib import messages 
from home.models import  Project
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# ######################################

def home_view(request, user_id):
    gr= Group.objects.filter(user=user_id)

    prj= Project.objects.filter(group__in=gr).filter(status="Incomplete")
    prjDone= Project.objects.filter(group__in=gr).filter(status="Complete")
    prjTotal= Project.objects.filter(group__in=gr)
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

def profile_view(request,username):
    user=User.objects.get(username=username)
    profile= Profile.objects.get(user=user.id)
    context={
        'profile':profile
    }
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

def createProject_view(request, username):
    form_prj=createProjectForm()
    if request.method=='POST':
        form_prj=createProjectForm(request.POST)
        if form_prj.is_valid():
            form_prj.save()
            messages.success(request, "Success")
            url = reverse('home', username)
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
            return redirect('/')
    context={'form':form}
    return render(request,'project/projectUpdate.html',context)

def deleteProject(request, id):
    project= Project.objects.get(id=id)
    if request.method=='POST':
        project.delete()
        return redirect('/')
        
    context={'project':project}
    return render(request,'project/confirm-delete.html',context)
    
def detailProject(request,project_id):
    prj= Project.objects.get(id=project_id)
    task_obj= Task.objects.filter(project=prj.id)
    
    context={
        'project':prj,
        'task':task_obj
    }
    return render(request,'project/projectDetail.html',context)




# ######################################

def group_view(request):
    return render(request,'user/group.html')

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

