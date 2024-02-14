def entidade_agencia(db_item) -> dict:
    return {
        'id': str(db_item['_id']),
        'nome_agencia': db_item['nome_agencia'],
        'cnpj': db_item['cnpj'],
        'email':db_item['email'],
        'telefone':db_item['telefone'],
        'cep':db_item['cep']
    }

def lista_entidade_agencia(db_item_lista) -> list:
    lista_agencias=[]
    for agencia in db_item_lista:
        lista_agencias.append(entidade_agencia(agencia))
    return lista_agencias