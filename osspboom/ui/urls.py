from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('view_details/', views.view_details, name='view_details'),
]