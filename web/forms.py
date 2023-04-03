from django import forms
from django.contrib.auth import get_user_model

from web.models import Book, Genre

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "total_pages", "count", "price", "genres", "publisher", "authors", "isbn")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class BookIdForm(forms.Form):
    book_id = forms.IntegerField()


class GenreIdForm(forms.Form):
    genre_id = forms.IntegerField()
