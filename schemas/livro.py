from pydantic import BaseModel

class LivroCreate(BaseModel):
    nome: str
    genero: str
    num_paginas: str
    autor: str
    editora: str
    preco: float

class LivroRead(BaseModel):
    id: int
    nome: str
    genero: str
    num_paginas: str
    autor: str
    editora: str
    preco: float

class LivroReadAll(BaseModel):
    livros: list[LivroRead]

class LivroUpdate(BaseModel):
    nome: str
    genero: str
    num_paginas: str
    autor: str
    editora: str
    preco: float

