from django.db import models
from django.utils import timezone
# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    made_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name