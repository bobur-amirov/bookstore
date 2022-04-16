from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from book.models import Book, Category, Author, Language
from comment.forms import CommentForm
from comment.models import Comment, Like


def book_list(request):
    ordering = request.GET.get('ordering')
    if ordering:
        books = Book.objects.all().order_by(ordering)
    else:
        books = Book.objects.all()

    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)

    context = {
        'books': page_obj,
        'range': range(1, 6)
    }

    return render(request, 'book/book_list.html', context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    comment_rating = Comment.objects.filter(book=book)
    book_categories = Book.objects.filter(category__book=book)
    summa = 0
    k = 0
    for i in comment_rating:
        summa += i.rating
        k += 1
    try:
        avg_summa = round(summa / k)
    except ZeroDivisionError:
        avg_summa = 0
    book.rating_avg = avg_summa
    book.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form_comment = form.save(commit=False)
            form_comment.book = book
            form_comment.user = request.user
            form_comment.rating = int(request.POST['rating'])
            form_comment.save()
            return redirect('book_detail', slug=book.slug)
    else:
        form = CommentForm()

    context = {
        'book': book,
        'form': form,
        'range': range(1, 6),
        'book_categories': book_categories,
    }

    return render(request, 'book/book_detail.html', context)


def likes(request):
    slug = request.POST.get('post')
    user = request.user
    book = Book.objects.get(slug=slug)
    current_like = book.likes

    liked = Like.objects.filter(user=user, book=book).count()

    if not liked:
        like = Like.objects.create(user=user, book=book)
        # like.save()
        current_like += 1
    else:
        like = Like.objects.filter(user=user, book=book)
        like.delete()
        current_like -= 1
    book.likes = current_like
    book.save()

    return redirect('book_detail', book.slug)


def category_books(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)

    context = {
        'category': category,
        'books': books,
        'range': range(1, 6),
    }

    return render(request, 'book/filter_books.html', context)


def author_books(request, slug):
    author = Author.objects.get(slug=slug)
    books = Book.objects.filter(authors=author)

    context = {
        'author': author,
        'books': books,
        'range': range(1, 6),
    }

    return render(request, 'book/filter_books.html', context)


def language_books(request, slug):
    language = Language.objects.get(slug=slug)
    books = Book.objects.filter(language=language)

    context = {
        'language': language,
        'books': books,
        'range': range(1, 6),
    }

    return render(request, 'book/filter_books.html', context)
