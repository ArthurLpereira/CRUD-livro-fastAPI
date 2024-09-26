from fastapi import APIRouter

from schemas.livro import (
    LivroCreate,
    LivroRead,
    LivroReadAll,
    LivroUpdate,
)
from models.livros import livrosDB

livro_router = APIRouter()

@livro_router.post(path="/livros", response_model=LivroRead)
def criar_livro(novo_livro: LivroCreate):
    novo_livro = livrosDB(
    nome = novo_livro.nome,
    genero = novo_livro.genero,
    num_paginas = novo_livro.num_paginas,
    autor = novo_livro.autor,
    editora = novo_livro.editora,
    preco = novo_livro.preco,
    )
    novo_livro.save()

    return novo_livro

@livro_router.get(path="/livros/{id_livro}", response_model=LivroRead)
def ler_um_livro(id_livro: int):
    livro = livrosDB.get_or_none(livrosDB.id == id_livro)
    return livro

@livro_router.get(path="/livros", response_model=LivroReadAll)
def ler_todos_os_livros():
    livros = livrosDB.select()
    return {'livros': livros}

@livro_router.patch(path="/livros/{id_livro}", response_model=LivroRead)
def atualizar_livro(id_livro: int, livro_atualizado: LivroUpdate):
    livro = livrosDB.get_or_none(livrosDB.id == id_livro)
    livro.nome = livro_atualizado.nome
    livro.genero = livro_atualizado.genero
    livro.num_paginas = livro_atualizado.num_paginas
    livro.autor = livro_atualizado.autor
    livro.editora = livro_atualizado.editora
    livro.preco = livro_atualizado.preco
    livro.save()

    return livro

@livro_router.delete(path="/livros/{id_livro}", response_model=LivroRead)
def deletar_livro(id_livro: int):
    livro = livrosDB.get_or_none(id_livro)
    livro.delete_instance()
    return livro
