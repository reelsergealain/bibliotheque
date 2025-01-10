from django.shortcuts import render
from books.models import Books
from books.forms import BookForm

def index(request):
    books = Books.objects.filter(quantity__gt=0)
    form = BookForm()
    return render(request, 'books/index.html', {'books': books, 'form': form})


def add_book(request):
    if request.method == 'POST':
        forms = BookForm(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = BookForm()
    return render(request, 'books/index.html', {'form': forms})