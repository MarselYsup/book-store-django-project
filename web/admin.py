from django.contrib import admin
from .models import Genre, Publisher, Book, Author
# Register your models here.
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)