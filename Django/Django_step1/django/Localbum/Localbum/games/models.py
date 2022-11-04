from django.db import models
# модель - считай что чертеж, так как он определяет структуру данных и все последующие настройки
#кастомная модель (т.е. таблица для бд)
class Product(models.Model):
    #соответсвенно столбцы и строки ,с их типами данных
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()

