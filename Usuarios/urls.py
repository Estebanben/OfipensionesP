from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.estudiantes_list,name='estudiantes_list')
]