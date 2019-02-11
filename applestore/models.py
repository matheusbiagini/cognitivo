"""Import models."""
from django.db import models


class Application(models.Model):
    """Model Application."""

    application_id = models.IntegerField()
    track_name = models.TextField()
    n_citacoes = models.IntegerField()
    size_bytes = models.BigIntegerField()
    price = models.FloatField()
    prime_genre = models.CharField(max_length=150)
