from django.db import models


class Prioridad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.upper()


class Remainder(models.Model):

    PRIORIDADES = (
        ("AT", "Alta"),
        ("NR", "Normal"),
        ("BJ", "Baja"),
    )

    MEDIA_CHOICES = (
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=7, choices=PRIORIDADES)
    prioridad_personal = models.ForeignKey(Prioridad, on_delete=models.CASCADE, default=1)
    fecha_creacion_g = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Remainder N° " + str(self.id) + ": " + self.titulo

