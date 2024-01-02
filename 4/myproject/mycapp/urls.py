from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('Profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('Profile/create/', views.profile_create, name='profile_create'),
    path('Profile/<int:pk>/update/', views.profile_update, name='profile_edit'),
    path('Profile/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
    path('preferences/', views.prefences_list, name='preferences_list'),
    path('preferences/<int:pk>/', views.preferences_detail, name='preferences_detail'),
    path('preferences/create/', views.preferences_create, name='preferences_create'),
    path('prefrences/<int:pk>/update/', views.preferences_edit, name='preferences_edit'),
    path('preferences/<int:pk>/delete/', views.preferences_delete, name='preferences_delete')
]
