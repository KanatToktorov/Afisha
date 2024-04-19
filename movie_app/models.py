from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Movie (models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='movies',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.movie.title} - {self.text}"

