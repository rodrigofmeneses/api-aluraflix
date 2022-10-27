def validate_keys_request_body(data: dict) -> bool:
    '''Verifica se todos os campos da requisição são válidos'''
    if set(data.keys()) == set(['id', 'titulo', 'descricao', 'url']):
        return True
    return False

def validade_fields_request_body(data: dict) -> bool:
    '''Verifica se todos os campos estão preenchidos'''
    for key, value in data.items():
        if not value:
            return False
    return True

def validate_json(data: dict) -> bool:
    '''Verifica se um JSON é valido'''
    return all(
        [validate_keys_request_body(data), validade_fields_request_body(data)]
    )