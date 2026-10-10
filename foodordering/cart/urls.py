from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/update/<int:id>/', views.cart_update, name='cart_update'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
]
