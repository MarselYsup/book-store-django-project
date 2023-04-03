from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_view, name="main"),
    path("registration/", views.registration_view, name="registration"),
    path("auth/", views.auth_view, name="auth"),
    path("logout/", views.logout_view, name="logout"),
    path("books/", views.books_view, name="books"),
    path("profile/", views.profile_view, name="profile"),
    path("bookform/", views.book_add_view, name="bookform"),
    path("adminbooks/", views.admin_books_view, name="adminbooks"),
    path("admingenres/", views.admin_genres_view, name="admingenres"),
    path("update-genre", views.admin_genres_update_view, name="admin_genres_update"),
]