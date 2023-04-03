from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render

from web.forms import RegistrationForm, AuthForm, BookIdForm, BookForm, GenreIdForm
from web.models import Book, UserProfile, Genre

# Create your views here.

User = get_user_model()


def main_view(request):
    return render(request, "web/main.html")


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            user_profile = UserProfile(
                user=user,
                amount=0
            )
            user_profile.save()
            is_success = True
    return render(request, "web/registration.html", {
        "form": form, "is_success": is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main")


@login_required
def books_view(request):
    if not request.user.is_superuser:
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        if request.method == 'POST':
            form = BookIdForm(data=request.POST)
            if form.is_valid():
                book = Book.objects.get(pk=form.cleaned_data["book_id"])
                if book.price > user_profile.amount:
                    form.add_error(None, "У вас недостаточно средств!")
                else:
                    book.count = book.count - 1
                    user_profile.amount = user_profile.amount - book.price
                    user_profile.books.add(book)
                    book.save()
                    user_profile.save()

        books = Book.objects.all()
        return render(request, "web/books.html", {"books": books, "amount": user_profile.amount})
    else:
        return redirect("main")


@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get(user_id=request.user.id)
    return render(request, "web/profile.html", {"books": user_profile.books, "amount": user_profile.amount})


@staff_member_required
def book_add_view(request):
    form = BookForm()
    is_success = False
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            is_success = True
    return render(request, "web/book_add.html", {
        "form": form, "is_success": is_success
    })


@staff_member_required
def admin_books_view(request):
    if request.method == 'POST':
        form = BookIdForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.get(pk=form.cleaned_data["book_id"])
            if book.count != 0:
                book.count = book.count - 1
                book.save()
            else:
                form.add_error(None, "Удалять книгу больше нельзя!")

    books = Book.objects.all()
    return render(request, "web/admin_books.html", {"books": books})


@staff_member_required
def admin_genres_view(request):
    if request.method == 'POST':
        form = GenreIdForm(data=request.POST)
        if form.is_valid():
            genre = Genre.objects.get(pk=form.cleaned_data["genre_id"])
            genre.delete()
    elif request.method == 'PUT':
        form = GenreForm(data=request.PUT)
        if form.is_valid():
            form.save()
    genres = Genre.objects.all()
    return render(request, "web/admin_genres.html", {"genres": genres})


@staff_member_required
def admin_genres_update_view(request):
    if request.method == 'POST':
        genre = Genre.objects.get(pk = request.POST["id"])
        genre.genre = request.POST["genre"]
        genre.save()
    genres = Genre.objects.all()
    return redirect("admingenres")