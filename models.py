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
        return f"Pedido('{self.origem}', '{self.destino}', '{self.data_ida}', '{self.horario_ida}', '{self.data_retorno}', '{self.horario_retorno}', '{self.tipo_veiculo}', '{self.guia}')"