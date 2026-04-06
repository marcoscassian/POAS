from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI()

class Livro(BaseModel):
    id: int
    nome: str

class Usuario(BaseModel):
    id: int
    nome: str


class Emprestimo(BaseModel):
    id: int
    usuario_id: int
    livro_id: int
    data_emprestimo: date
    data_devolucao: date
    devolvido: bool = False

livros: List[Livro] = []
usuarios: List[Usuario] = []
emprestimos: List[Emprestimo] = []

# crud livros

@app.post("/livros")
def criar_livro(livro: Livro):
    livros.append(livro)
    return {"mensagem": "Livro criado com sucesso", "livro": livro}

@app.get("/livros")
def listar_livros():
    return livros

@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int):
    for livro in livros:
        if livro.id == livro_id:
            return livro
    return {"erro": "Livro não encontrado"}

@app.put("/livros/{livro_id}")
def atualizar_livro(livro_id: int, novo_livro: Livro):
    for i, livro in enumerate(livros):
        if livro.id == livro_id:
            novo_livro.id = livro_id
            livros[i] = novo_livro
            return {"mensagem": "Livro atualizado", "livro": novo_livro}
    return {"erro": "Livro não encontrado"}

@app.delete("/livros/{livro_id}")
def deletar_livro(livro_id: int):
    for i, livro in enumerate(livros):
        if livro.id == livro_id:
            livros.pop(i)
            return {"mensagem": "Livro removido"}
    return {"erro": "Livro não encontrado"}

# crud usuarios

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return {"mensagem": "Usuário criado", "usuario": usuario}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    return {"erro": "Usuário não encontrado"}

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, novo_usuario: Usuario):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            novo_usuario.id = usuario_id
            usuarios[i] = novo_usuario
            return {"mensagem": "Usuário atualizado", "usuario": novo_usuario}
    return {"erro": "Usuário não encontrado"}

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios.pop(i)
            return {"mensagem": "Usuário removido"}
    return {"erro": "Usuário não encontrado"}

# emprestimo

@app.post("/emprestimos")
def fazer_emprestimo(emprestimo: Emprestimo):
    emprestimos.append(emprestimo)
    return {"mensagem": "Empréstimo realizado", "emprestimo": emprestimo}

@app.put("/emprestimos/{emprestimo_id}/devolver")
def devolver_livro(emprestimo_id: int):
    for e in emprestimos:
        if e.id == emprestimo_id:
            e.devolvido = True
            return {"mensagem": "Livro devolvido"}
    return {"erro": "Empréstimo não encontrado"}

@app.get("/emprestimos/atrasados")
def listar_atrasados():
    hoje = date.today()

    atrasados = [
        e for e in emprestimos
        if not e.devolvido and e.data_devolucao < hoje
    ]

    return atrasados
