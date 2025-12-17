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
        "valor": 1670.00,
        "vencimento": "2025-10-15"
    }

@app.get("/meiospagamento")
def verificar():
    return [
        {
        "meio": "PIX",
        "código para pagamento pix": "00020126580014br.gov.bcb.pix0136a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z600170014br.gov.bcb.pix0210pagador@email.com5204000053039865802BR5912Nome",
        "valor": 1680.00,
        "vencimento": "2025-12-30"
        },
        {
        "meio": "BOLETO",
        "link de pagamento do boleto": "banco.bradesco.com",
        "valor": 1672.00,
        "vencimento": "2026-01-10"
        }
    ]
