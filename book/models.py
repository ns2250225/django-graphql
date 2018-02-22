# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="作者姓名")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.ForeignKey(Title, related_name='book_title', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='book_author', on_delete=models.CASCADE)