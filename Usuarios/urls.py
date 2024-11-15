from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('hijos/',views.hijos_del_padre,name='hijos_del_padre')
]