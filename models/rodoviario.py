from pydantic import BaseModel

class Rodoviario(BaseModel):
    nome_rodoviario: str
    cnpj: str
    cep: str
    email: str
    telefone: str
    categoria_transporte: list