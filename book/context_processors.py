from book.models import Category, Author, Language


def category(request):
    categories = Category.objects.all()

    return {'categories': categories}


def author(request):
    authors = Author.objects.all()

    return {'authors': authors}


def lungauge(request):
    lengauges = Language.objects.all()

    return {'lengauges': lengauges}
