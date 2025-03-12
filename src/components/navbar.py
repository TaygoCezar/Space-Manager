import flet as ft

def navbar():
    """Retorna o componente navbar. São passados os estilos para 
    a personalização do componente. 
    """
    return ft.Container(
        ft.Row(
            [
                ft.Text("SPACE MANAGER", **styles["navbar-title"]),
                ft.Row(
                    [
                        ft.TextButton("Reservas", **styles["navbar-button"]),
                        ft.TextButton("Espaços", **styles["navbar-button"]),
                        ft.Container(**styles["navbar-divider"]),
                        ft.IconButton(ft.Icons.INFO_OUTLINE, **styles["navbar-icon-button"]),
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
    },

    "navbar-button": {
        "style": ft.ButtonStyle(
            color="white",
            text_style=ft.TextStyle(size=18)
        )
    },
    "navbar-icon-button": {
        "icon_color": "white",
        "icon_size": 22
    }
}