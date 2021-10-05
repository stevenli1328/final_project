from django.urls import path, re_path

from . import views

app_name='profile'
urlpatterns = [
	path('', views.user_profile, name = 'profile'),
    path('logout/', views.logout_user, name='logout'),
    re_path(r'.*', views.other, name = 'bad link')
]