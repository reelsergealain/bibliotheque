from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:book_id>/', views.book_detail, name='book_detail'),
    # path('author/', views.author_list, name='author_list'),
    # path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    # path('author/<int:author_id>/books/', views.author_books, name='author_books'),
    # path('search/', views.search, name='search'),
]