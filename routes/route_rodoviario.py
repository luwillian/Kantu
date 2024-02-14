from fastapi import APIRouter
from config.database import conexao
from models.rodoviario import Rodoviario
from bson import ObjectId
from schema.schema_rodoviario import lista_entidade_rodoviario, entidade_rodoviario

rodoviario_router = APIRouter()

#pega todas as rodoviarios
@rodoviario_router.get('/rodoviario')
async def lista_rodoviarios():
    return lista_entidade_rodoviario(conexao.Kantu.Rodoviario.find())

#busca uma unica rodoviario por id
@rodoviario_router.get('/rodoviario/{rodoviario_id}')
async def busca_rodoviario_id(rodoviario_id):
    return entidade_rodoviario(conexao.Kantu.Rodoviario.find_one({
        '_id': ObjectId(rodoviario_id)
    }))

#cadastra uma rodoviario
@rodoviario_router.post('/rodoviario/cadastrar')
async def cadastra_rodoviario(rodoviario:Rodoviario):
    conexao.Kantu.Rodoviario.insert_one(dict(rodoviario))
    return lista_entidade_rodoviario(conexao.Kantu.Rodoviario.find({
        'nome_rodoviario': rodoviario.nome_rodoviario
    }))

#atualiza rodoviario
@rodoviario_router.put('/rodoviario/atualizar/{rodoviario_id}')
async def atualiza_rodoviario(rodoviario_id, rodoviario:Rodoviario):
    conexao.Kantu.Rodoviario.find_one_and_update(
        {
            '_id': ObjectId(rodoviario_id)
        },
        {
            '$set':dict(rodoviario)
        }
    )
    return entidade_rodoviario(
        conexao.Kantu.Rodoviario.find_one(
            {
                '_id': ObjectId(rodoviario_id)
            }
        )
    )

#exclui rodoviario
@rodoviario_router.delete('/rodoviario/deletar/{rodoviario_id}')
async def deleta_rodoviario(rodoviario_id):
    return entidade_rodoviario(
        conexao.Kantu.Rodoviario.find_one_and_delete(
            {
                '_id': ObjectId(rodoviario_id)
            }
        )
    )
