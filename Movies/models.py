from django.db import models
import datetime
from django.contrib.auth.models import User


class Movie(models.Model):
    movie_name = models.TextField()
    image_url = models.TextField()
    ratings = models.TextField()
    date = models.DateField('Date', default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name

# Create your models here.
