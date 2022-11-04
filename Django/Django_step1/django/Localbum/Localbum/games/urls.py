from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name ="home"),
    path('games/', views.games, name ="games"),
    path('example/', views.example, name='example'),
    path('TIAR/',views.TIAR,name="TIAR")
    ]
