from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name="add"),
    path('list/', views.student_list, name="list"),
    path('delete/<int:id>/', views.delete_student, name="delete"),
]
