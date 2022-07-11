"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('loginfail/', views.LoginfailView.as_view(), name='loginfail'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('sitemap/', views.SitemapView.as_view(), name='sitemap'),
]