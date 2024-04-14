"""
URL configuration for chanlee_crud_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from chanleecrud.views import home, save_data, delete_data, edit_data, course, course_save_data, course_edit_data

# URL patter specifies a view function which then determines the contents of the page
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('course/', course, name='course'),
    path('add/', course_save_data, name='course_save_data'),
    path('course_edit/', course_edit_data, name='course_edit_data'),
    path('save/', save_data, name='save'),
    path('delete/', delete_data, name='delete'),
    path('edit/', edit_data, name='edit'),
]
