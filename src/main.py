import flet as ft

import router

def main(page: ft.Page) -> None:
    """Inicializa a aplicação.
    """
        
    router.init(page)
    page.window.min_width = 1200
    page.window.min_height = 800

    page.title = "Space Manager"
    page.theme_mode = "light"
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(windows=ft.PageTransitionTheme.NONE)
    )

    page.fonts = {
        "Saira Extra Condensed - Regular": "/fonts/SairaExtraCondensed-Regular.ttf",
        "Saira Extra Condensed - Bold": "/fonts/SairaExtraCondensed-Bold.ttf"
    }

    page.go("reservas")

if __name__ == "__main__":
    ft.app(main)