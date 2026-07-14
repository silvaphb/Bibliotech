from typing import List
from ninja import NinjaAPI
from .models import Book
from django.forms.models import model_to_dict
from .schemas import BookIn, BookOut, BookUpdate


api = NinjaAPI()


@api.get('/livros', response={200: List[BookOut]})
def view_books(request):
    books = list(Book.objects.all().values())
    return books

@api.post('/livro', response={201: BookOut})
def new_book(request, book: BookIn):
    try:
        if Book.objects.filter(title=book.title).exists():
            return {'Error': 'Livro já existente!'}
        new_book = Book(title=book.title, author=book.author, description=book.description, publication=book.publication, category=book.category, stock=book.stock)
        new_book.save()
        return BookOut.from_domain(new_book)
    except Exception as error:
        return {'Error': error}

@api.post('/remover_livro', response={200: bool})
def delete_book(request, id: int):
    try:
        if not Book.objects.filter(id=id).exists():
            return False
        
        book = Book.objects.get(id=id)
        book.delete()
        return True
    except Exception as error:
        return False

@api.patch('/atualizar_livro', response={200: BookOut})
def update_book(request, id: int, book: BookUpdate):
    try:
        if not Book.objects.filter(id=book.id).exists():
            return False
        
        updated_book = Book.objects.get(id=id)
        for attr, value in book.dict().items():
            setattr(update_book, attr, value)

        updated_book.save()
        return BookOut.from_domain(updated_book)
    
    except Exception as error:
        return False
