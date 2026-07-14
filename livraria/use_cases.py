from .repositories import IBookRepository
from .entity import BookEntity
from .dto import BookInDTO, BookOutDTO, BookUpdateDTO
from .repository import BookRepository

class RegisterBookUseCase:
    def __init__(self, book_repo: IBookRepository):
        self.book_repo = book_repo
    
    def execute(self, book: BookInDTO) -> BookOutDTO | None:
        if self.book_repo.verify_exists(title=book.title):
            return None
        
        data = BookEntity(
            id=book.id,
            title=book.title,
            author=book.author,
            description=book.description,
            publication=book.publication,
            category=book.category,
            stock=book.stock
        )

        self.book_repo.save(book=data)
        return BookOutDTO.from_domain(model=book)
    
class ReturnBookUseCase:
    def __init__(self, book_repo: IBookRepository):
        self.book_repo = book_repo

    def execute(self, id: int) -> BookOutDTO:
        book = self.book_repo.get_unique(id)
        return BookOutDTO.from_domain(book)