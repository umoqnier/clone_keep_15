from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^contacto/$', contacto),
]





"""
Tareas para mañana (Muy obligatorias)

1.Tener instalado Pgadmin4
  |
  |---> Por lo tanto postgresql
2.Tener el formulario hecho
3.psycopg2 (pip install psycopg2)
4.Ser felices :)

"""


















