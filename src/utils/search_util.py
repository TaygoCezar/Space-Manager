import re


def ignore_case(value: str) -> str:
    """Converte a string para um formato onde as diferenças entre maiúsculas e minúsculas são ignoradas.

    Args:
        value (str): String a ser convertida.

    Returns:
        str: String convertida.
    """
    return value.lower()


def ignore_accent_marks(value: str) -> str:
    """Converte a string para um formato onde as letras acentuadas são convertidas para suas versões não acentuadas.

    Args:
        value (str): String a ser convertida.

    Returns:
        str: String convertida.
    """
    value = re.sub(r"[àáâã]", "a", value)
    value = re.sub(r"[éê]", "e", value)
    value = re.sub(r"[í]", "i", value)
    value = re.sub(r"[óôõ]", "o", value)
    value = re.sub(r"[ú]", "u", value)
    value = re.sub(r"[ç]", "c", value)
    value = re.sub(r"[ñ]", "n", value)
    
    return value


def prefix_check(value: str, prefix: str) -> bool:
    """Verifica se a string possui o prefixo passado, ignorando diferenças entre maiúsculas e minúsculas e letras acentuadas.

    Args:
        value (str): String a ser verificada.
        prefix (str): Prefixo a ser verificado.

    Returns:
        bool: True se a string possuir o prefixo, False caso contrário.
    """
    prefix = ignore_accent_marks(ignore_case(prefix))
    value = ignore_accent_marks(ignore_case(value))
    return value.startswith(prefix)