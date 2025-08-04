from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    made_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    made_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    TYPE_MEALS = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=100, choices=TYPE_MEALS)
    servings = models.PositiveIntegerField(default=1)
    date_consumed = models.DateField()

    def total_calories(self):
        return self.food.calories * self.servings

    def __str__(self):
        return f"{self.user.username} - {self.meal_type}: {self.food.name}"