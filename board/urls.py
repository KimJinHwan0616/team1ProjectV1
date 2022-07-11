from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsView.as_view(), name='news'),
    path('announce/', views.AnnounceView.as_view(), name='announce'),
    path('teamplayer/', views.TeamplayerView.as_view(), name='teamplayer'),
    path('news_detail/', views.News_detailView.as_view(), name='news_detail'),
    path('announce_detail/', views.Announce_detailView.as_view(), name='announce_detail'),
    path('teamplayer_detail/', views.Teamplayer_detailView.as_view(), name='teamplayer_detail'),
]