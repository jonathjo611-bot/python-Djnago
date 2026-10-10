from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_detail, name='artist-detail'),
]
