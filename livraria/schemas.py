from typing import Optional
from ninja import Schema

class BookIn(Schema):
    title: str
    author: str
    description: str
    publication: str
    category: str
    stock: int

class BookOut(Schema):
    id: int
    title: str
    author: str
    description: str
    publication: str
    category: str
    stock: int

    @staticmethod
    def from_domain(model):
        return BookOut(
            id = model.id,
            title = model.title,
            author = model.author,
            description = model.description,
            publication = model.publication,
            category = model.category,
            stock = model.stock
        )

class BookUpdate(Schema):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    publication: Optional[str] = None
    category: Optional[str] = None
    stock: Optional[int] = None
    