from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_registrations, name='view_registrations'),
    path('create/', views.create_registration, name='create_registration'),
    path('update/<int:pk>/', views.update_registration, name='update_registration'),
    path('delete/<int:pk>/', views.delete_registration, name='delete_registration'),
]