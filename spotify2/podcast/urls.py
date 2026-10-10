from django.urls import path
from . import views

urlpatterns = [
    path('', views.podcast_list, name='podcast'),
    path('<int:id>/', views.podcast_detail, name='podcast_detail'),
]
