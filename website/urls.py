from django.urls import path

from . import views

urlpatterns = [

  path('', views.homepage, name = 'homepage'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    #path('tasks/', views.tasks, name = 'tasks'),
    #path('time_off/', views.time_off, name = 'time off'),
    #path('login/', views.login, name = 'login'),
    #path('payroll/', views.payroll, name = 'payroll'),
    #re_path(r'.*', views.other, name = 'bad link')

]