import flet as ft
from utils import route

<<<<<<< HEAD
from routes import espacos, espacos_adicionar, reservas, sobre
=======
# Utils
from utils.route_util import parse_route

# Páginas
from routes.reservas_route import reservas
from routes.reservas_adicionar_route import reservas_adicionar
from routes.reservas_editar_route import reservas_editar
from routes.espacos_route import espacos
from routes.espacos_adicionar_route import espacos_adicionar
from routes.espacos_editar_route import espacos_editar
from routes.sobre_route import sobre

# Rotas devem retornar uma tupla com duas funções:
# 1. Função de inicialização, que será chamada toda vez que a página for acessada
# 2. View da página
>>>>>>> stable


def init(p: ft.Page) -> None:
    """Inicializa o roteador e carrega as rotas da aplicação.

<<<<<<< HEAD
    Args:
        p (ft.Page): Objeto da página.
    """

    global page, routes
=======
    # Rotas
    routes = {
        "reservas": reservas(page),
        "reservas_adicionar": reservas_adicionar(page),
        "reservas_editar": reservas_editar(page),

        "espacos": espacos(page),
        "espacos_adicionar": espacos_adicionar(page),
        "espacos_editar": espacos_editar(page),

        "sobre": sobre(page)      
    }    
>>>>>>> stable
    
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

<<<<<<< HEAD
    name, params = route.parse(e.route)

    if name not in routes:
        raise ValueError(f"Rota {name} não encontrada.")

    page.views.clear() # Limpa as views da página
    routes[name]["on_start"](**params) # Chama a função ao_iniciar da página e passa os parâmetros
    page.views.append(routes[name]["view"]) # Adiciona a view da página
=======
    route_name, params = parse_route(e.route) # Converte a rota em nome e parâmetros, veja src/utils/route.py
    
    # Verifica se a rota existe, caso contrário, lança um erro
    if route_name not in routes:
        raise ValueError(f"Rota {route_name} não encontrada.")
    
    # Ações necessárias para a navegação:
    page.views.clear() # Limpa as views da página

    routes[route_name][0](**params) # Chama a função init da página, passando os parâmetros da rota
    page.views.append(routes[route_name][1]) # Adiciona a view da página
    
>>>>>>> stable
    page.update() # Atualiza a página