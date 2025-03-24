def parse_route(route: str) -> tuple[str, dict[str, str]]:
    """Converte uma string de rota em seu nome e parâmetros.

    Args:
        route (str): String de rota a ser convertida. (ex: "reservas_editar?id=1")
    """
    route = route.split("?")
    route_name = route[0]

    params = {}
    if len(route) == 2:
        params = dict([param.split("=") for param in route[1].split("&")])

    return route_name, params