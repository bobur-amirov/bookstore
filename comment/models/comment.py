from django.db import models

from account.models import Account
from book.models import Book


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.book.name
