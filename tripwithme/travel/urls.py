
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('smart_planner/', views.smart_planner),
    path('mytrip/', views.mytrip),
]
