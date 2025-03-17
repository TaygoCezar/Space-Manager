import flet as ft

from components.main import main


def load(page: ft.Page) -> tuple:
    """Carrega a página de adicionar espaços.

    Args:
        page (ft.Page): Objeto da página.

    Returns:
        tuple: Nome da página, função de inicialização e view.
    """

    def handle_start() -> None:
        """Função executada ao iniciar a página.
        """

    return "espacos_adicionar", handle_start, main(
        "espacos_adicionar",
        "Adicionar Espaço",
        "espacos",
        controls=[

        ]
    )


styles = {

}