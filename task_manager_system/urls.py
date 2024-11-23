"""
URL configuration for task_manager_system.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from task_manager import views  # Importing views from the task_manager app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', views.dashboard, name='dashboard'),  # Home page view
]

