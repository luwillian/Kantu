from pydantic import BaseModel

class DadosPessoais(BaseModel):
    email_corporativo: str
    celular: str
    nome: str
    cpf: str






