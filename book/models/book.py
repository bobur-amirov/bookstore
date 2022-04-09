from decimal import Decimal

from django.db import models

from .author import Author
from .category import Category
from .language import Language


class Book(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    cover = models.ImageField(upload_to='book/')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    authors = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    rating_avg = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    @property
    def price2(self):
        return round(self.price - self.price * Decimal('0.2'), 2)

class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='book/images')

    def __str__(self):
        return self.book.name
