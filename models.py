from app import db
from enum import Enum

class TipoVeiculosEnum(Enum):
    ONIBUS = "ONIBUS"
    VAN = "VAN"
    MICRO_ONIBUS = "MICRO_ONIBUS"

class PEDIDOS(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    id_agencia = db.Column(db.Integer, nullable=False)
    origem = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    data_ida = db.Column(db.Date, nullable=False)
    horario_ida = db.Column(db.String(100), nullable=False)
    data_retorno = db.Column(db.Date, nullable=False)
    horario_retorno = db.Column(db.String(100), nullable=False)
    tipo_veiculo = db.Column(db.Enum(TipoVeiculosEnum), nullable=False)
    guia = db.Column(db.Enum, nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f"Pedido('{self.origem}', '{self.destino}',\
              '{self.data_ida}', '{self.horario_ida}', '{self.data_retorno}', \
                '{self.horario_retorno}', '{self.tipo_veiculo}', '{self.guia}')"
    
class AGENCIA(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    cadastur = db.Column(db.String(20), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f"Agencia('{self.nome}', '{self.cnpj}',\
              '{self.cadastur}', '{self.cep}', '{self.rua}', \
                '{self.numero}', '{self.bairro}', '{self.cidade}', '{self.estado}', '{self.telefone}', '{self.email}', '{self.senha}')"
