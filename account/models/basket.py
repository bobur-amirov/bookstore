from django.db import models

from account.models.user import Account
from book.models import Book


class Basket(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return self.book.name
