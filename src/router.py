import flet as ft
from utils import route

from routes import espacos, espacos_adicionar, reservas, sobre


def init(p: ft.Page) -> None:
    """Inicializa o roteador e carrega as rotas da aplicação.

    Args:
        p (ft.Page): Objeto da página.
    """

    global page, routes
    
    page = p
    routes = load_routes()


def load_routes() -> dict:
    """Carrega as rotas da aplicação.

    Returns:
        dict: Dicionário de rotas.
    """

    pages = [espacos, espacos_adicionar, reservas, sobre]
    return{
        name: {
            "on_start": handle_start,
            "view": view
        } for name, handle_start, view in [p.load(page) for p in pages]
    }


def handle_navigation(e: ft.RouteChangeEvent) -> None:
    """Gerencia a navegação entre as páginas da aplicação.

    Args:
        e (ft.RouteChangeEvent): Evento de mudança de rota.

    Raises:
        ValueError: Rota não encontrada.
    """

    name, params = route.parse(e.route)

    if name not in routes:
        raise ValueError(f"Rota {name} não encontrada.")

    page.views.clear() # Limpa as views da página
    routes[name]["on_start"](**params) # Chama a função ao_iniciar da página e passa os parâmetros
    page.views.append(routes[name]["view"]) # Adiciona a view da página
    page.update() # Atualiza a página