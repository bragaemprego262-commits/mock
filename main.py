from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Requisicao(BaseModel):
    cpf: str

@app.post("/verificar")
def verificar(req: Requisicao):
    cpf = req.cpf
    ultimo = int(cpf[-1])
    tem_pendencia = ultimo % 2 == 0

    if tem_pendencia:
        return {
            "status": "PENDENTE",
            "mensagem": "O cliente possui pendências financeiras ativas e necessita regularização."
        }
    else:
        return {
            "status": "OK",
            "mensagem": "Nenhuma pendência encontrada para este CPF."
        }
