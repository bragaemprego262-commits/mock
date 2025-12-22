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

@app.get("/options")
def opcoes():
    return {
        "status": "PENDENTE",
        "mensagem": "O cliente possui pendências financeiras ativas e necessita regularização.",
        "cpf": "11112398712",
        "valor_original": 1670.00,
        "vencimento": "2025-10-15",
        "opcoes": [
            {
                "id": 1,
                "descricao": "Pagamento à vista com 15% de desconto",
                "total": 1419.5,
                "detalhes": "Totalizando R$ 1419.5"
            },
            {
                "id": 2,
                "descricao": "Parcelamento em 3 vezes",
                "total": 1732.5,
                "valor_parcela": 577.5,
                "primeiro_pagamento": "2024-06-05",
                "detalhes": "3 parcelas de R$ 577.5"
            },
            {
                "id": 3,
                "descricao": "Parcelamento em 6 vezes",
                "total": 1815.0,
                "valor_parcela": 302.5,
                "primeiro_pagamento": "2024-06-05",
                "detalhes": "6 parcelas de R$ 302.5"
            }
        ]
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
