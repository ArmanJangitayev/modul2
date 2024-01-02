from django.urls import path
from . import views
urlpatterns = [
    path('', views.SaleList, name='sale_list'),
    path('purchase/<int:pk>/', views.PurchaseDetail, name='purchase_detail'),
    path('sale/<int:pk>/', views.SaleDetail, name='sale_detail'),
    path('transaction/<int:pk>/', views.TransactionDetail, name='transaction_detail'),
    path('transaction/create/', views.TransactionCreate, name='transaction_create'),
    path('sale/create/', views.SaleCreate, name='sale_create'),
    path('purchase/create/', views.PurchaseCreate, name='purchase_create'),
    path('sale/<int:pk>/delete/', views.SaleDelete, name='sale_delete'),
    path('purchase/<int:pk>/delete/', views.PurchaseDelete, name='purchase_delete'),
    path('transaction/<int:pk>/delete/', views.TransactionDelete, name='transaction_delete'),

]
