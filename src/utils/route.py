def parse(route: str) -> tuple[str, dict[str, str]]:
    """Decompõe a rota em nome e parâmetros.

    Args:
        rota (str): Rota a ser decomposta.

    Returns:
        tuple[str, dict[str, str]]: Nome da rota e parâmetros.
    """

    segments = route.split("?")
    name = segments[0]
    params = {}

    if len(segments) > 1:
        params = dict([parametro.split("=") for parametro in segments[1].split("&")])

    return name, params