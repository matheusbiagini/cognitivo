from django.db import models

class Application(models.Model):
    application_id = models.IntegerField()
    track_name = models.CharField(max_length=100)
    n_citacoes = models.IntegerField()
    size_bytes = models.IntegerField()
    price = models.FloatField()
    prime_genre = models.CharField(max_length=50)
