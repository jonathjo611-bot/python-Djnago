from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate),
    path('history/', views.history),
]
