from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsView.as_view(), name='news'),
    path('announce/', views.AnnounceView.as_view(), name='announce'),
    path('teamplayer/', views.TeamplayerView.as_view(), name='teamplayer'),
    path('news_detail/', views.News_detailView.as_view(), name='news_detail'),
    path('detail/', views.DetailView.as_view(), name='detail'),
    path('detail2/', views.Detail2View.as_view(), name='detail2'),
]