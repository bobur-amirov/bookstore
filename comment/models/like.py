from django.db import models

from account.models import Account
from book.models import Book


class Like(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.name
