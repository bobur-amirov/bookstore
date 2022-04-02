from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='author/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
