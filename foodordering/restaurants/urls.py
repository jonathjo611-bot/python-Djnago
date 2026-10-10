from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='home'),
    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
]
