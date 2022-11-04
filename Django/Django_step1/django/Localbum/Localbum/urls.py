"""Localbum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# базовая настройка админки
# для подробной инфы о роуетерах(маршрутизаторах) и видах смотреть файл  serializers.py
from django.contrib import admin
# include - добавление к задаваемому пути ,новые параметры
from django.urls import path, include
# для создания дальнешейго перехода по категориям
from rest_framework.routers import DefaultRouter
# виды(т.е. доступные способы взаимодействия с моделью)
from Localbum.games.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', ProductViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('Localbum.games.urls'))
]
