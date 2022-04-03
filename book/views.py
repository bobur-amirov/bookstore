from django.shortcuts import render, get_object_or_404

from book.models import Book


def book_list(request):
    ordering = request.GET.get('ordering')
    if ordering:
        books = Book.objects.all().order_by(ordering)
    else:
        books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'book_list.html', context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    context = {
        'book': book
    }

    return render(request, 'book_detail.html', context)
