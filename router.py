from flet import Page
from flet import RouteChangeEvent

from routes.home import home

def init(p: Page) -> None:
    """Inicialização das páginas da aplicação.
    
    Args:
        p (Page): Objeto da página.
    """
    global page, routes
    page = p

    # Rotas
    routes = {
        "home": home(page)
    }    
    
def navigate(e: RouteChangeEvent) -> None:
    """Gerencia a navegação entre as páginas da aplicação.

    Args:
        e (RouteChangeEvent): Evento de mudança de rota
    """

    if e.route not in routes:
        raise ValueError(f"Rota {e.route} não encontrada.")
        
    page.views.clear()
    page.views.append(routes[e.route])
    page.update()