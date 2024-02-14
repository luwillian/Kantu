def entidade_rodoviario(db_item) -> dict:
    return {
        'id': str(db_item['_id']),
        'nome_rodoviario': db_item['nome_rodoviario'],
        'cnpj': db_item['cnpj'],
        'email':db_item['email'],
        'telefone':db_item['telefone'],
        'cep':db_item['cep'],
        'categoria_transporte':list(db_item['categoria_transporte'])
    }

def lista_entidade_rodoviario(db_item_lista) -> list:
    lista_rodoviario=[]
    for rodoviario in db_item_lista:
        lista_rodoviario.append(entidade_rodoviario(rodoviario))
    return lista_rodoviario
