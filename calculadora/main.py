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

#rota: /soma : recebe dois inteiros A e B e retorna o resultado
@app.get('/soma')
def soma(a:int, b:int)-> str:
    resultado = a + b
    return f"A soma dos valores é {resultado}"

#- rota: /subtracao : recebe dois inteiros A e B e retorna o resultado
@app.get('/subtracao')
def soma(a:int, b:int)-> str:
    resultado = a - b
    return f"A subtracão dos valores é {resultado}"

#- rota: /divisao : recebe dois inteiros A e B e retorna o resultado
@app.get('/divisao')
def soma(a:int, b:int)-> str:
    resultado = a / b
    return f"A divisão dos valores é {resultado}"

#- rota: /multiplicacao : recebe dois inteiros A e B e retorna o resultado
@app.get('/multiplicacao')
def soma(a:int, b:int)-> str:
    resultado = a * b
    return f"A multiplicação dos valores é {resultado}"

#- rota: /raiz : recebe um inteiro e retorna o resultado da raiz quadrada

@app.get('/raiz')
def raiz(a:int)-> str:
    resultado = a ** 0.5
    return f"A raiz de {a} é {resultado}"
