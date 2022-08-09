from django.db import models

# Create your models here.
class Moviedata(models.Model):

    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length = 200)
    durations = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200,default='action')