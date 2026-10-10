from django.urls import path
from . import views

urlpatterns = [
    path('', views.podcast_detail, name='podcast-detail'),
]
