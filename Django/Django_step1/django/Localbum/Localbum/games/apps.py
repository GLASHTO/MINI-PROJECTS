from django.apps import AppConfig
#приложения и пути к ним(абсолютный путь, т.е. начиная с ветки в которой находится файл запуска)

class GamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Localbum.games'
