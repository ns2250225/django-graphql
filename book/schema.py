# -*- coding: utf-8 -*-

import graphene
from graphene_django.types import DjangoObjectType

from .models import Book, Title, Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class TitleType(DjangoObjectType):
    class Meta:
        model = Title


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author



# 定义动作，类似POST, PUT, DELETE
class BookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    author = graphene.String(required=True)

class CreateBook(graphene.Mutation):
    # api的输入参数
    class Arguments:
        book_data = BookInput(required=True)
    
    # api的响应参数
    ok = graphene.Boolean()
    book = graphene.Field(BookType)
    
    # api的相应操作，这里是create
    def mutate(self, info, book_data):
        title = Title.objects.create(title=book_data['title'])
        author = Author.objects.create(name=book_data['author'])
        book = Book.objects.create(title=title, author=author)
        ok = True
        return CreateBook(book=book, ok=ok)


# 定义查询，类似GET
class Query(object):
    all_books = graphene.List(BookType)
    all_titles = graphene.List(TitleType)
    all_authors = graphene.List(AuthorType)

    def resolve_all_books(self, info, **kwargs):
        # 查询所有book的逻辑
        return Book.objects.all()

    def resolve_all_titles(self, info, **kwargs):
        # 查询所有title的逻辑
        return Book.objects.select_related('book_title').all()

    def resolve_all_authors(self, info, **kwargs):
        # 查询所有author的逻辑
        return Book.objects.select_related('book_author').all()

