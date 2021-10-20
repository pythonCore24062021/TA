from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text


metadata = MetaData()
authors_table = Table('authors',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))
books_table = Table('books', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))
class Author:

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name


class Book:

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title

mapper(Book, books_table)
mapper(Author, authors_table, properties = {'books': relation(Book, backref='author')})


