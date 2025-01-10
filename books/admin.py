from django.contrib import admin
from .models import Author, Books, Category

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name']
    

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'quantity', 'published_date', 'isbn']
    search_fields = ['title', 'author__name']
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name']
