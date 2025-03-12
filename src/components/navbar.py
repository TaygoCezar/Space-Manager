import flet as ft

def navbar(route: str = "") -> ft.Container:
    """Retorna o componente navbar. São passados os estilos para 
    a personalização do componente. 
    """

    dynamic_styles = {
        "navbar-button-reservas": {
            "style": ft.ButtonStyle(
                color="white",
                text_style=ft.TextStyle(
                    size=18,
                    weight=ft.FontWeight.BOLD if route == "reservas" else ft.FontWeight.NORMAL
                )
            )
        },
        "navbar-button-espacos": {
            "style": ft.ButtonStyle(
                color="white",
                text_style=ft.TextStyle(
                    size=18,
                    weight= ft.FontWeight.BOLD if route == "espacos" else ft.FontWeight.NORMAL
                )
            )
        },
        "navbar-icon-button": {
            "icon": ft.Icons.INFO if route == "sobre" else ft.Icons.INFO_OUTLINE,
            "icon_color": "white",
            "icon_size": 22
        }
    }

    def goto_reservas(e):
        if route != "reservas":
            e.control.page.go("reservas")

    def goto_espacos(e): 
        if route != "espacos": 
            e.control.page.go("espacos")
    
    def goto_sobre(e):
        if route != "sobre":
            e.control.page.go("sobre")            
            
    return ft.Container(
        ft.Row(
            [
                ft.Text("SPACE MANAGER", **styles["navbar-title"]),
                ft.Row(
                    [
                        ft.TextButton("Reservas", on_click=goto_reservas, **dynamic_styles["navbar-button-reservas"]),
                        ft.TextButton("Espaços", on_click=goto_espacos, **dynamic_styles["navbar-button-espacos"]),
                        ft.Container(**styles["navbar-divider"]),
                        ft.IconButton(on_click=goto_sobre, **dynamic_styles["navbar-icon-button"]),
                    ],
                    **styles["navbar-nav"]
                )
            ],
            **styles["navbar-row"]
        ),
        **styles["navbar-container"]
    )


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
    }
}
