from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
]
