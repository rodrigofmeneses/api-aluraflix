def validate_keys_request_body_put(data: dict) -> bool:
    '''Verifica se todos os campos da requisição são válidos'''
    return set(data.keys()) == set(['id', 'titulo', 'descricao', 'url'])

def validate_keys_request_body_patch(data: dict) -> bool:
    '''Verifica se todos os campos da requisição são válidos'''
    return set(data.keys()).issubset(set(['id', 'titulo', 'descricao', 'url']))
        
def validade_fields_request_body(data: dict) -> bool:
    '''Verifica se todos os campos estão preenchidos'''
    for _, value in data.items():
        if not value:
            return False
    return True

def validate_json(data: dict, method: str='POST') -> bool:
    '''Verifica se um JSON é valido dado um método'''
    match method:
        case 'PUT' | 'POST':
            return all(
                [
                    validate_keys_request_body_put(data), 
                    validade_fields_request_body(data)
                ]
            )

        case 'PATCH':
            return all(
                [
                    validate_keys_request_body_patch(data),
                    validade_fields_request_body(data)
                ]
            )
        case _:
            return False