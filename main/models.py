from django.db import models
from datetime import timezone
from user.models import MyUser


class Genre(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='movies')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/")
    added = models.DateTimeField(auto_now_add=True)
    year = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title


class MovieImage(models.Model):
    image = models.ImageField(upload_to='shots', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')
