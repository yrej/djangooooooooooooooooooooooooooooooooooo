from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='cover_images/')

    def __str__(self):
        return self.title


class LibraryEntry(models.Model):
    STATUS_CHOICES = [
        ('O', 'Owned'),
        ('W', 'Wishlist'),
        ('C', 'Completed'),
        ('P', 'Playing'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')
    added_on = models.DateField(auto_now_add=True)
    completed_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.title} - {self.get_status_display()}"
