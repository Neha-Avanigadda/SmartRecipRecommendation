from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    youtube_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

