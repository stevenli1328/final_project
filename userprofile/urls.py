from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.user_profile, name = 'profile'),
    re_path(r'.*', views.other, name = 'bad link')
]