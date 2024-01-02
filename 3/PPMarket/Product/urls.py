from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('Product/<int:pk>/', views.product_detail, name='product_detail'),
    path('Product/create/', views.product_create, name='product_create'),
    path('Product/<int:pk>/update/', views.product_update, name='product_edit'),
    path('Product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('search/', views.search_products, name='search_products'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete')
]
