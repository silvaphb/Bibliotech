from .repositories import IBookRepository
from .entity import BookEntity

from typing import List

from .models import Book

class BookRepository(IBookRepository):
    def save(self, book: BookEntity) -> BookEntity:
        Book.objects.update_or_create(
            id=book.id,
            defaults={
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'publication': book.publication,
                'category': book.category,
                'stock': book.stock
            }
        )
        return book
    
    def verify_exists(self, title: str) -> bool:
        return Book.objects.filter(title=title).exists()

    def get_unique(self, id: int) -> BookEntity | None:
        book = Book.objects.get(id=id)
        if not book:
            return None
        return self._to_model(book)

    def search_all(self) -> List[BookEntity]:
        books = Book.objects.all()
        return [self._to_model(book) for book in books]
    
    def delete(self, id: int) -> None:
        try:
            Book.objects.get(id=id).delete()
            return None
        except Book.DoesNotExist:
            return None
    
    def _to_model(self, book) -> BookEntity:
        return BookEntity(
            id=book.id,
            title=book.title,
            author=book.author,
            description=book.description,
            publication=book.publication,
            category=book.category,
            stock=book.stock
        )