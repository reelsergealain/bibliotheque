from django.shortcuts import render
from books.models import Books

def index(request):
    books = Books.objects.filter(quantity__gt=0)
    return render(request, 'books/index.html', {'books': books})