from django.contrib import admin
#кастомная модель - импорт для того чтобы админ мог напрямую редактировать данные
from Localbum.games.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
