def decompor(rota: str) -> tuple[str, dict[str, str]]:
    """Decompõe a rota em nome e parâmetros.

    Args:
        rota (str): Rota a ser decomposta.

    Returns:
        tuple[str, dict[str, str]]: Nome da rota e parâmetros.
    """

    partes = rota.split("?")
    nome = partes[0]
    parametros = {}

    if len(partes) > 1:
        parametros = dict([parametro.split("=") for parametro in partes[1].split("&")])

    return nome, parametros