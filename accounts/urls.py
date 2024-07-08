from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("products/", views.products),
    # adding url param 'pk_test'
    path('customer/<str:pk_test>/', views.customer),
]
