from django.urls import path
from . import views

urlpatterns = [
    path('', views.watchlist, name="watchlist"),
    path('add/<int:id>/', views.add, name="add"),
    path('remove/<int:id>/', views.remove, name="remove"),
]
