from pydantic import BaseModel

class Agencia(BaseModel):
    nome_agencia: str
    cnpj: str
    email: str
    telefone: str
    cep: str

