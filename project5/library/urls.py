from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name="books"),
    path('book/<int:id>/', views.book_detail, name="detail"),
]
