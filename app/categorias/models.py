from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=300)
	descripcion = models.CharField(null=True, blank=True, max_length=300)
	icono = models.ImageField(max_length=200, help_text=u"Resolución optima 50x50 px")
	orden = models.IntegerField(null=True, blank=True)
	indice = models.PositiveSmallIntegerField(default=1)
	texto_sms = models.CharField(
        verbose_name='Nombre SMS',
        max_length=160,
        null=True, blank=True,
    )