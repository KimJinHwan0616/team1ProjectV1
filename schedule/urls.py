"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('kl1/', views.KL1View.as_view(), name='KL1'),
    path('kl2/', views.KL2View.as_view(), name='KL2'),
]