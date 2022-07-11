
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('stadium/', views.TeamsView.as_view(), name='stadium'),
]
