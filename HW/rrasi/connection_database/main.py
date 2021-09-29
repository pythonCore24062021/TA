from services import AuthorService, BookService


books = BookService.get_all()
print(books)
print(BookService.get_by_id(6).author.books)