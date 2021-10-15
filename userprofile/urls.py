from django.urls import path, re_path

from . import views

app_name='profile'
urlpatterns = [
	path('', views.user_profile, name = 'profile'),
    path('login/', views.login_user, name='login'),
    #path('edit/'), views.edit_user, name='edit'),
    path('logout/', views.logout_user, name='logout'),
    re_path(r'.*', views.other, name = 'bad link')
]