from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='orders'),
    path('orders/<int:id>/', views.order_track, name='order_track'),
    path('orders/<int:id>/advance/', views.order_advance, name='order_advance'),
]
