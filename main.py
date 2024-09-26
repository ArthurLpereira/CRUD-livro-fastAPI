from fastapi import FastAPI

from config.database import start_database, end_database
from routers.livro import livro_router
app = FastAPI()

app.add_event_handler(event_type='startup', func=start_database)
app.add_event_handler(event_type='shutdown', func=end_database)

app.include_router(router=livro_router, tags=['LIVROS'])