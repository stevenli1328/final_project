from django.urls import path, re_path

from . import views

app_name='profile'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<str:username>/', views.user_profile, name='profile'),
    re_path(r'.*', views.other, name = 'bad link')
]