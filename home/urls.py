from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('<int:user_id>/', views.home_view, name='home'),
   path('signup/', views.register_view, name='signup'),
   path('focus-study/',views.pomodoro_view,name='pomodoro'), 
   path('group/', views.group_view, name='group'),
   
   path('profile/<str:username>/', views.profile_view, name='profile'),
   path('edit-profile/<str:username>/', views.editProfile, name='edit-profile'),
   
   path('createproject/<str:username>/', views.createProject_view, name='createProject'),
   path('update/<int:id>/', views.updateProject, name='update'),
   path('delete/<int:id>/', views.deleteProject, name='delete'),
   path('detail/<int:project_id>/', views.detailProject, name='detail'),

   path('create-task/<int:project_id>/', views.createTask, name='createTask'),
   path('update-task/<int:task_id>/', views.updateTask, name='updateTask'),

   # path( 'login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
   path( 'login/',views.login_view, name='login'),
   path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)