from django.urls import path, re_path

from . import views

app_name='payroll'

urlpatterns = [
	path('', views.payroll, name = 'payroll'),
    path('createpayroll/', views.createpayroll, name='newpayroll'),
    path('<int:payroll_pk>', views.viewpayroll, name='viewpayroll'),
    re_path(r'.*', views.bad, name = 'bad link'),  
]