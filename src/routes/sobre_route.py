import flet as ft

from components.main import main

<<<<<<< HEAD:src/routes/sobre.py

def load(page: ft.Page) -> tuple:
    """Carrega a página sobre.

    Args:
        page (ft.Page): Objeto da página.

    Returns:
        tuple: Nome da página, função de inicialização e view.
    """

    def handle_start() -> None:
        """Função executada ao iniciar a página.
        """

    return "sobre", handle_start, main(
        "sobre",
        "Sobre",
=======

def sobre(page: ft.Page):
    """Página Sobre
    
    Página com informações sobre o projeto e os integrantes.

    Args:
        page (ft.Page): Página atual

    Returns:
        function: Função de inicialização
        ft.View: Página Sobre
    """

    # Inicialização
    def init():
        pass

    # Página
    return init, ft.View(
>>>>>>> stable:src/routes/sobre_route.py
        controls=[

        ]
    )


<<<<<<< HEAD:src/routes/sobre.py
=======
# Estilos
>>>>>>> stable:src/routes/sobre_route.py
styles = {

}