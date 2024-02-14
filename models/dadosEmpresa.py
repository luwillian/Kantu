from pydantic import BaseModel


class DadosEmpresa(BaseModel):
    cnpj: str
    categoria: str
    