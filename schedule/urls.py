from django.urls import path, re_path

from . import views

app_name='schedule'
urlpatterns = [
	path('', views.schedule, name = 'schedule'),
    path('eventsFeed', views.eventsFeed, name='events'),
    path('delete/<int:schedule_pk>/', views.deleteschedule, name='deleteschedule'),
    path('newtimeoff/', views.timeoffrequest, name='newtimeoff'),
    path('timeoff/', views.timeoff, name='timeoff'),
    path('timeoff/<int:timeoff_pk>/', views.approvetimeoff, name='approvetimeoff'),
    path('<int:schedule_pk>/', views.editschedule, name='editschedule'),
    path('createschedule/', views.createschedule, name='newschedule'),
    re_path(r'.*', views.bad, name = 'bad link'),
]