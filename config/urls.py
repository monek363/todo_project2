"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from tasks import views as task_main
from users import views as user_main

urlpatterns = [
    path('', task_main.main , name="main" ),
    path('register', user_main.register , name="register" ),
    path('login', user_main.login , name="login" ),
    path('logout', user_main.logout, name="logout" ),
    path('index', task_main.index , name="profile" ),
    path('task/create', task_main.create_task, name="create_task"),
    path('task/<int:task_id>/toggle', task_main.toggle_task, name="toggle_task"),
    path('task/<int:task_id>/delete', task_main.delete_task, name="delete_task"),
    path("admin/", admin.site.urls),
]

