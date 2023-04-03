from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Publisher(models.Model):
    name = models.CharField(max_length=255)


class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    total_pages = models.IntegerField(default=1)
    count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(auto_now=True)
    isbn = models.CharField(max_length=13)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    books = models.ManyToManyField(Book)