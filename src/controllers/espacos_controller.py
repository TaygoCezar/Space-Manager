import flet as ft

# Servicos
from services.espacos_service import Espaco, get_all_espacos

# Utils
from utils.search_util import prefix_check


def get_espacos_by_key(key: str) -> list[Espaco]:
    """Retorna todos os espacos que possuem algum campo com o prefixo da chave passada, ignorando diferenças entre maiúsculas e minúsculas, e letras acentuadas.

    Args:
        key (str): Chave para a busca.

    Returns:
        list[Espaco]: Lista de espacos que possuem algum campo com o prefixo da chave passada.
    """
    espacos = get_all_espacos()

    def filter_espacos(espaco: Espaco) -> bool:
        return any([prefix_check(value, key) for value in espaco.values()]) # Verifica se algum campo do espaco possui o prefixo da chave passada. Verifique a função prefix_check no arquivo utils/search_utils.py
    
    return list(filter(filter_espacos, espacos))


def validate_nome(nome: str) -> str|None:
    """Verifica se o nome do espaco é válido.

    Args:
        nome (str): Nome do espaco.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """

    if nome == "":
        return "O campo 'Nome' é obrigatório"
    
    return None


def validate_codigo(codigo: str, exclude_codigo: str|None=None) -> str|None:
    """Verifica se o código do espaco é válido.

    Args:
        codigo (str): Código do espaco.
        exclude_codigo (str, optional): Código a ser excluído da verificação. Defaults to None.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """
    if codigo == "":
        return "O campo 'Código' é obrigatório"
    
    for espaco in get_all_espacos():
        if espaco["codigo"] == codigo and espaco["codigo"] != exclude_codigo:
            return "Código já cadastrado"
    
    return None