from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Requisicao(BaseModel):
    cpf: str

@app.get("/verificar")
def verificar():
    return {
        "status": "PENDENTE",
        "mensagem": "O cliente possui pendências financeiras ativas e necessita regularização.",
        "valor": 1650.00,
        "vencimento": "2023-10-15"
    }

@app.get("/meiospagamento")
def verificar():
    return [
        {
        "meio": "PIX",
        "endereco": "O cliente possui pendências financeiras ativas e necessita regularização.",
        "valor": 1650.00,
        "vencimento": "2023-10-15"
        },
        {
        "meio": "BOLETO",
        "endereco": "O cliente possui pendências financeiras ativas e necessita regularização.",
        "valor": 1613.00,
        "vencimento": "2023-10-10"
        }
    ]
