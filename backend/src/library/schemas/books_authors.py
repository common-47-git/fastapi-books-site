from src.library.schemas.authors import AuthorBase, AuthorRead
from src.library.schemas.books import BookBase, BookRead

class AuthorsBooks(AuthorBase):
    author_books: list["BookRead"] | None = []
    
class BooksAuthors(BookBase):
    book_authors: list["AuthorRead"] | None = []
