from django.shortcuts import render
# базовые модели
from django.contrib.auth.models import User, Group
# установка видов
from rest_framework import viewsets
# сериалайзеры
from Localbum.serializers import UserSerializer, GroupSerializer, ProductSerializer
# кастомная модель
from Localbum.games.models import Product
from django.http import HttpResponse


# для подробной инфы о видах смотреть файл  serializers.py
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# вид для кастомной модели
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# def main(request):
#     return HttpResponse('<h4>Hello motherfucker</h4>')

def main(request):
    return render(request, 'games/main.html')


def games(request):
    return render(request, 'games/games.html')


def example(request):
    return render(request, 'games/example.html')

def TIAR(request):
    return render(request,"games/ThreeInARow.html")