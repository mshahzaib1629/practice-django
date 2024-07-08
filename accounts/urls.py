from django.urls import path

from . import views

urlpatterns = [
    # we can add name to the routes, which can be used for in-app routing
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    # adding url param 'pk_test'
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
