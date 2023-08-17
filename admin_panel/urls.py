"""
URL configuration for admin_panel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('',views.loginpage, name='loginpage'),
    path('signup',views.signup, name='signup'),
    path('userHome', views.user_home, name='userHome'),
    path('logout', views.logout, name='logout'),
    path('adminlogin', views.admin_login, name='adminLogin'),
    path('adminHome', views.admin_home, name='adminHome'),
    path('deleteUser<int:id>', views.delete_user, name='deleteUser'),
    path('editUser<int:id>', views.edit_user, name='editUser'),
    path('updateData<int:id>', views.update_data, name='updateData'),
    path('adduser', views.add_user,name='adduser'),


]
