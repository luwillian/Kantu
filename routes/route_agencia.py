from fastapi import APIRouter
from config.database import conexao
from models.agencia import Agencia
from bson import ObjectId
from schema.schema_agencia import lista_entidade_agencia, entidade_agencia

agencia_router = APIRouter()

#pega todas as agencias
@agencia_router.get('/agencia')
async def lista_agencias():
    return lista_entidade_agencia(conexao.Kantu.Agencia.find())

#busca uma unica agencia por id
@agencia_router.get('/agencia/{agencia_id}')
async def busca_agencia_id(agencia_id):
    return entidade_agencia(conexao.Kantu.Agencia.find_one({
        '_id': ObjectId(agencia_id)
    }))

#cadastra uma agencia
@agencia_router.post('/agencia/cadastrar')
async def cadastra_agencia(agencia:Agencia):
    conexao.Kantu.Agencia.insert_one(dict(agencia))
    return lista_entidade_agencia(conexao.Kantu.Agencia.find({
        'nome_agencia': agencia.nome_agencia
    }))

#atualiza agencia
@agencia_router.put('/agencia/atualizar/{agencia_id}')
async def atualiza_agencia(agencia_id, agencia:Agencia):
    conexao.Kantu.Agencia.find_one_and_update(
        {
            '_id': ObjectId(agencia_id)
        },
        {
            '$set':dict(agencia)
        }
    )
    return entidade_agencia(
        conexao.Kantu.Agencia.find_one(
            {
                '_id': ObjectId(agencia_id)
            }
        )
    )

#exclui agencia
@agencia_router.delete('/agencia/deletar/{agencia_id}')
async def deleta_agencia(agencia_id):
    return entidade_agencia(
        conexao.Kantu.Agencia.find_one_and_delete(
            {
                '_id': ObjectId(agencia_id)
            }
        )
    )
