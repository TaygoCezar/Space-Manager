import flet as ft

from components.main import main
from components.forms.button_filled import button_filled


def load(page: ft.Page) -> tuple:
    """Carrega a página de espaços.

    Args:
        page (ft.Page): Objeto da página.

    Returns:
        tuple: Nome da página, função de inicialização e view.
    """

    def handle_start() -> None:
        """Função executada ao iniciar a página.
        """

    return "espacos", handle_start, main(
        "espacos",
        "Espaços",
        controls=[
            ft.Row([
                button_filled("Adicionar Espaco", "add", lambda e: e.control.page.go("espacos_adicionar")),
            ])
        ]
    )


styles = {

}