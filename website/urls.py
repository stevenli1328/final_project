from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.homepage, name = 'homepage'),
    path('signup/', views.signupuser, name = 'signupuser'),
    path('time_off/', views.time_off, name = 'time off'),
    path('payroll/', views.payroll, name = 'payroll'),
    re_path(r'.*', views.other, name = 'bad link')
]
