from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist'),
    path('<int:id>/', views.artist_detail, name='artist_detail'),
]
