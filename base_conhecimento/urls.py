from django.urls import path
from . import views 

urlpatterns = [
    path('', views.base_conhecimento, name='base_conhecimento'),
    path('buscar_defeito/', views.buscar_defeito, name='buscar_defeito'),
    path('buscar/', views.buscar_defeito, name='buscar_defeito'),
]