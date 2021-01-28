"""Pegado app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import (
    home_view, 
    material_create_view,
    PaymentCreateView, PaymentListView,
    ClientCreateView, ClientDeleteView, ClientDetailView, ClientListView, ClientUpdateView,
    ProductCreateView,ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView,
    WorkerCreateView, WorkerListView, WorkerUpdateView, WorkerDetailView, WorkerDeleteView
    )

app_name = "pegado"
urlpatterns = [
    path('worker/', WorkerListView.as_view(), name="worker-list"),
    path('worker/<int:pk>/', WorkerDetailView.as_view(), name="worker-detail"),
    path('worker/<int:pk>/update', WorkerUpdateView.as_view(), name="worker-update"),
    path('worker/<int:pk>/delete', WorkerDeleteView.as_view(), name="worker-delete"),
    path('worker/create/', ProductCreateView.as_view(), name="worker-create"),
    path('product/', ProductListView.as_view(), name="product-list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name="product-update"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product-delete"),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('client/', ClientListView.as_view(), name="client-list"),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name="client-update"),
    path('client/<int:pk>/delete', ClientDeleteView.as_view(), name="client-delete"),
    path('client/create/', ClientCreateView.as_view(), name="client-create"),
    path('material/create/', material_create_view, name="material-create"),
    path('payment/create/', PaymentCreateView.as_view(), name="payment-create"),
    path('payment/', PaymentListView.as_view(), name="payment-list")
    

]
