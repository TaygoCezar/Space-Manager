import flet as ft

import router

def main(page: ft.Page) -> None:
    """Inicializa a aplicação.
    """
        
    router.init(page)
    page.title = "Space Manager"
    page.theme_mode = "light"

    page.fonts = {
        "Saira Extra Condensed - Bold": "/fonts/SairaExtraCondensed-Bold.ttf"
    }

    page.go("reservas")

if __name__ == "__main__":
    ft.app(main)