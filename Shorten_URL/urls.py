"""Shorten_URL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('autenticacion/', views.autenticacion, name='autenticacion'),
    path('shorten_url/', views.shorten_url, name='shorten_url'),
    path('my_url/', views.my_url, name='my_url'),
    path('mostrar/url/<int:url_id>/', views.mostrar_url, name='mostrar_url'),
    path('eliminar/<int:url_id>/', views.eliminar, name='eliminar'),
    path('eliminar/user/', views.eliminar_user, name='eliminar_user'),
    path('salir/', views.salir, name='salir'),
]
