import flet as ft

# Páginas da aplicação
from routes.reservas import reservas
from routes.espacos import espacos
from routes.sobre import sobre

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
        "reservas": reservas(page), # -> (init, view)
        "espacos": espacos(),
        "sobre": sobre()
    }    
    
def navigate(e: ft.RouteChangeEvent) -> None:
    """Gerencia a navegação entre as páginas da aplicação.

    Args:
        e (RouteChangeEvent): Evento de mudança de rota
    """

    if e.route not in routes:
        raise ValueError(f"Rota {e.route} não encontrada.")
        
    page.views.clear()
    routes[e.route][0]() # -> chama a função init da rota
    page.views.append(routes[e.route][1])
    page.update()