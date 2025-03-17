import flet as ft

from components.main import main


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
        controls=[

        ]
    )


styles = {

}