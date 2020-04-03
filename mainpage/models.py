from django.db import models


# Create your models here.
class Do(models.Model):
    things = models.TextField()
