from ninja import NinjaAPI
from livraria.api.views import api

app = NinjaAPI(title='Bibliotech')

app.add_router('/api', api, tags=['Livros'])