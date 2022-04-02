from django.shortcuts import render

from book.models import Book


def home(request):
    books = Book.objects.all().order_by('-created')

    context = {
        'books': books
    }

    return render(request, 'home.html', context)
