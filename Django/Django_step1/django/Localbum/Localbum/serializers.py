# базовые модели джанго
from django.contrib.auth.models import User, Group
# наследуемый класс для создания сериалайзера
from rest_framework import serializers
# кастомная модель (т.е. создана мной)))
from Localbum.games.models import Product


# примеры создания сериалайзеров
# сериализатор - преобразует данные модели в запрашиваемый тип, чаще всего это API
# вид - определяет функции доступные в созданной модели (api)
# маршрутизатор - определяет URL по запросу к которому предоставляется доступ к каждому виду
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
