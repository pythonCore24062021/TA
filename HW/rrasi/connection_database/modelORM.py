from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title

        self.description = description

        self.author = author

    def __repr__(self):
        return f"{self.id} {self.title}"
    def print(self):
        print(f"MY: {self.id} {self.title}")

#
#
DB_NAME = 'TAQC'
USER = 'postgres'
PASSWORD = 'HeckfyfHfczr#1511'
HOST = 'localhost'
PORT = '5432'
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
Session = sessionmaker(bind=engine) # bound session
session = Session()
#
author_1 = Author('Richard Dawkins')
author_2 = Author('Matt Ridley')
#
book_1 = Book('The Red Queen', 'A popular science book', author_2)
book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)
#
session.add(author_1)
session.add(author_2)
session.add(book_1)
session.add(book_2)
session.add(book_3)
#
session.commit()
#
session.query(Book).filter(Book.title)
print(session.query(Book).filter(Book.title == 'The Selfish Gene'))
print(session.query(Book).filter(Book.title == 'The Selfish Gene').all())
print(session.query(Book).filter(Book.title == 'The Selfish Gene').first())
b = session.query(Book).filter(Book.title == 'The Selfish Gene').first()
b.print()
