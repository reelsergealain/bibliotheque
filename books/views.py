from django.shortcuts import render
from books.models import Books
from forms import BookForm

def index(request):
    books = Books.objects.filter(quantity__gt=0)
    return render(request, 'books/index.html', {'books': books})


def add_book(request):
    forms = BookForm
    return render(request, 'books/index.html', {'form': forms})