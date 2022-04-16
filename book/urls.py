from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<slug:slug>', views.book_detail, name='book_detail'),
    path('like', views.likes, name='likes'),
    path('category/<slug:slug>', views.category_books, name='category_books'),
    path('author/<slug:slug>', views.author_books, name='author_books'),
    path('language/<slug:slug>', views.language_books, name='language_books'),
]
