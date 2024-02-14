from pydantic import BaseModel

class Pedidos(BaseModel):
    id_agencia: str
    email_comercial: str
    nome: str
    whatsapp: str
    cnpj: str
    destino: str
    endereco_saida: str
    endereco_retorno: str
    data_inicio: datetime
    data_fim: datetime
    tipo_transporte: str
    status: bool
    id_rodoviario: str