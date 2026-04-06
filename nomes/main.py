#pip install fastapi uvicorn
#uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Hello, world!"}

@app.get('/meunome')
def nome(nome:str)-> str:
    return f"Meu nome é{nome}"

@app.get('/soma')
def soma(soma:int)-> int:
    return f"Meu nome é{nome}"
#rota: /soma : recebe dois inteiros A e B e retorna o resultado

#- rota: /subtracao : recebe dois inteiros A e B e retorna o resultado

#- rota: /divisao : recebe dois inteiros A e B e retorna o resultado

#- rota: /multiplicacao : recebe dois inteiros A e B e retorna o resultado

#- rota: /raiz : recebe um inteiro e retorna o resultado da raiz quadrada
