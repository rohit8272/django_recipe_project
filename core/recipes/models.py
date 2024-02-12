from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_media')
