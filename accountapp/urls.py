from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accountapp'

urlpatterns = [
    path('', views.index, name ='test'),

]
 
# account/  
# account/a
# account/b  