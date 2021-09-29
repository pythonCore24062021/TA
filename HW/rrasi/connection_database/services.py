from modelORM import Book, Author
from connection_database import SESSION

print(dir())

__all__ = ["BookService", "AuthorService"]


class BookService:
    @staticmethod
    def get_all() -> Book:
        return SESSION.query(Book).all()

    staticmethod

    def get_by_id(id) -> Book:
        try:
            book = SESSION.query(Book).filter(Book.id == id).first()
            return book
        except:
            pass


class AuthorService:
    staticmethod

    def get_all(self) -> Book:
        return SESSION.query(Author).all()