from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Requisicao(BaseModel):
    cpf: str

@app.post("/verificar")
def verificar(req: Requisicao):
    cpf = req.cpf

    # Exemplo simples: se o último dígito do CPF é par, tem pendência
    ultimo = int(cpf[-1])
    tem_pendencia = (ultimo % 2 == 0)

    if tem_pendencia:
        return {
            "status": "PENDENTE",
            "mensagem": "O cliente possui pendências financeiras ativas e necessita regularização.",
            "valor": 1650.00,
            "vencimento": "2023-10-15"
        }
    else:
        return {
            "status": "OK",
            "mensagem": "Nenhuma pendência encontrada para este CPF."
        }
