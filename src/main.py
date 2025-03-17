import flet as ft
import roteador


def main(page: ft.Page) -> None:
    """Inicia a aplicação e define as configurações iniciais.

    Args:
        page (ft.Page): Objeto da página.
    """

    page.title = "Space Manager"
    page.theme_mode = "light"
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(windows=ft.PageTransitionTheme.NONE)
    )

    page.window.min_width = 1200
    page.window.min_height = 800

    page.fonts = {
        "Saira Extra Condensed - Regular": "/fonts/SairaExtraCondensed-Regular.ttf",
        "Saira Extra Condensed - Bold": "/fonts/SairaExtraCondensed-Bold.ttf"
    }

    roteador.inicializar(page)
    page.on_route_change = roteador.ao_navegar
    page.go("espacos")


if __name__ == "__main__":
    ft.app(main)