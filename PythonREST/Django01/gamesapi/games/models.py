from django.db import models

# Create your models here.
"""The Game class is a subclass of the django.db.models.Model class
    Each defined attribute represents a database column or field.
    Django automatically adds an autoincrement pkey.
    The class declares a Meta inner class that declares an ordering attribute
    and sets its value to a tuple of string whose first value is 'name', indicating
    that by default we want the results ordered by the name in ascending order.
"""
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
