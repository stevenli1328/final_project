from django.urls import path, re_path

from . import views

app_name='schedule'
urlpatterns = [
	path('', views.schedule, name = 'schedule'),
    path('eventsFeed', views.eventsFeed, name='events'),
    path('createschedule/', views.createschedule, name='newschedule'),
    re_path(r'.*', views.bad, name = 'bad link'),
]