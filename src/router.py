import flet as ft

# Páginas do aplicativo

from routes.reservas import reservas
from routes.espacos import espacos
from routes.sobre import sobre
from routes.reservas_adicionar import reservas_adicionar
from routes.reservas_editar import reservas_editar

def init(p: ft.Page) -> None:
    """Inicialização das páginas da aplicação.
    
    Args:
        p (Page): Objeto da página.
    """
    global page, routes
    page = p
    page.on_route_change = navigate

    # Rotas
    routes = {
        "reservas": reservas(page),
        "espacos": espacos(page),
        "sobre": sobre(page),
        "reservas_adicionar": reservas_adicionar(page),
        "reservas_editar": reservas_editar(page)
    }    
    
def navigate(e: ft.RouteChangeEvent) -> None:
    """Gerencia a navegação entre as páginas da aplicação.

    Args:
        e (RouteChangeEvent): Evento de mudança de rota
    """

    route = e.route.split("?")
    
    route_name = route[0]
    params = {} if len(route) == 1 else dict([param.split("=") for param in route[1].split("&")])
    
    if route_name not in routes:
        raise ValueError(f"Rota {route_name} não encontrada.")
        
    page.views.clear() # Limpa as views da página
    routes[route_name][0](**params) # Chama a função init da página
    page.views.append(routes[route_name][1]) # Adiciona a view da página
    page.update() # Atualiza a página