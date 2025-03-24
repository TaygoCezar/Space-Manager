import flet as ft

def navbar(route: str = "") -> ft.Container:
    """Retorna o componente navbar. 
    
    Args:
        route (str, optional): Rota atual. Defaults to "".

    Returns:
        ft.Container: Componente Navbar
    """

    # Eventos
    def goto(new_route: str):
        return lambda e: e.page.go(new_route)
    
    # Componente
    return ft.Container(
        ft.Row(
            [
                ft.Text("SPACE MANAGER", **styles["navbar-title"]),
                ft.Row(
                    [
                        ft.TextButton("Reservas", on_click=goto("reservas"), **styles["navbar-button-selected"] if route == "reservas" else styles["navbar-button"]),
                        ft.TextButton("Espaços", on_click=goto("espacos"), **styles["navbar-button-selected"] if route == "espacos" else styles["navbar-button"]),
                        ft.Container(**styles["navbar-divider"]),
                        ft.IconButton(on_click=goto("sobre"), **styles["navbar-icon-button-selected"] if route == "sobre" else styles["navbar-icon-button"]),
                    ],
                    **styles["navbar-nav"]
                )
            ],
            **styles["navbar-row"]
        ),
        **styles["navbar-container"]
    )

# Estilos
styles = {
    "navbar-container": {
        "padding": ft.padding.symmetric(15, 25),
        "bgcolor": "#003565"
    },
    "navbar-row": {
        "alignment": ft.MainAxisAlignment.SPACE_BETWEEN,
        "vertical_alignment": ft.CrossAxisAlignment.CENTER
    },

    "navbar-nav": {
        "vertical_alignment": ft.CrossAxisAlignment.CENTER,
        "spacing": 12
    },

    "navbar-title": {
        "color": "white",
        "size": 30,
        "weight": ft.FontWeight.BOLD,
        "font_family": "Saira Extra Condensed - Bold"
    },

    "navbar-divider": {
        "width": 0,
        "height": 24,
        "border": ft.border.all(1, "white")
    },

    "navbar-button": {
        "style": ft.ButtonStyle(
            color="white",
            text_style=ft.TextStyle(
                size=18,
                weight=ft.FontWeight.NORMAL
            )
        )
    },
    "navbar-button-selected": {
        "disabled": True,
        "style": ft.ButtonStyle(
            color="white",
            text_style=ft.TextStyle(
                size=18,
                weight=ft.FontWeight.BOLD
            )
        )
    },

    "navbar-icon-button": {
        "icon": ft.Icons.INFO_OUTLINE,
        "icon_color": "white",
        "icon_size": 22
    },
    "navbar-icon-button-selected": {
        "disabled": True,
        "icon": ft.Icons.INFO,
        "icon_color": "white",
        "icon_size": 22
    }
}
