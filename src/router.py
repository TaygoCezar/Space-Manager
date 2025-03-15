import flet as ft

# Páginas do aplicativo
"""
    Cada página do aplicativo é uma função que recebe um parâmetro:
    - page: Página da aplicação, utilizada para realizar navegação.
    
    Essa função deverá retornar uma tupla com duas funções:
    - init: Função executada antes da página ser exibida. A função init pode receber zero ou mais parâmetros.
        Os parâmetros passados para a função init serão obtidos através da rota passada para a função navigate.
        Separando a rota e os parâmetros por "#", e cada parâmetro separado por ",".
        
        Exemplo:
            page.go("editar_reserva#1") -> A função navigate irá navegar para página "editar_reserva" e passar o parâmetro "1" para a função init.

    - view: Página a ser exibida.
"""
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
        "reservas": reservas(page),
        "espacos": espacos(page),
        "sobre": sobre(page)
    }    
    
def navigate(e: ft.RouteChangeEvent) -> None:
    """Gerencia a navegação entre as páginas da aplicação.

    Args:
        e (RouteChangeEvent): Evento de mudança de rota
    """

    if e.route not in routes:
        raise ValueError(f"Rota {e.route} não encontrada.")
        
    page.views.clear() # Limpa as views da página
    routes[e.route][0]() # Chama a função init da página
    page.views.append(routes[e.route][1]) # Adiciona a view da página
    page.update() # Atualiza a página