from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Publisher(models.Model):
    name = models.CharField(max_length=255)


class Genre(models.Model):
    genre = models.CharField(max_length=100)


class Author(models.Model):
    first_name = models.CharField(255)
    middle_name = models.CharField(255)
    last_name = models.CharField(255)


class Book(models.Model):
    title = models.CharField(max_length=100)
    total_pages = models.IntegerField
    count = models.PositiveIntegerField
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField
    isbn = models.CharField(13)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    books = models.ManyToManyField(Book)