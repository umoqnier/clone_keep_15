from django.db import models

class Remainder(models.Model):

    PRIORIDADES = (
        ("AT", "Alta"),
        ("NR", "Normal"),
        ("BJ", "Baja"),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=7, choices=PRIORIDADES)
    fecha_creacion = models.DateTimeField(auto_now=True)



