from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.tasks, name = 'tasks'),
    path('createtask/', views.createtask, name='newtask'),
    re_path(r'.*', views.bad, name = 'bad link'),
]