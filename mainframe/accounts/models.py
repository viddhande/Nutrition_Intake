from django.db import models

class Current(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    meals_per_day = models.IntegerField()
    meal_portion_size = models.CharField(max_length=10)
    dietary_preference = models.CharField(max_length=10)
    lifestyle_preference = models.CharField(max_length=20)
    existing_health_condition = models.CharField(max_length=20, blank=True)
    physical_activity_level = models.CharField(max_length=10)
    existing_allergens = models.CharField(max_length=20, blank=True)
    carbohydrate_intake = models.CharField(max_length=10, blank=True)
    protein_intake = models.CharField(max_length=10, blank=True)
    fats_intake = models.CharField(max_length=10, blank=True)
