from django.urls import path
from . import views

urlpatterns = [
    path('', views.playlist_list, name='playlist'),
    path('liked/', views.liked_songs, name='liked'),
    path('like/<int:id>/', views.like, name='like'),
    path('<int:id>/', views.playlist_detail, name='playlist_detail'),
]
