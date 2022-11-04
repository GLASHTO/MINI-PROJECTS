#пробная команда получения данных с своей же бд
import requests as r
from django.core.management.base import BaseCommand
#доп комманды для терминала
class Command(BaseCommand):
    def handle(self, *args, **options):
        res = r.get('http://127.0.0.1:8000/products')
        print(res.json())
