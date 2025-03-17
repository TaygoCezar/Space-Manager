import flet as ft


def handle_click(e: ft.TapEvent) -> None:
    """Função executada ao clicar no botão. Redireciona para a rota.

    Args:
        e (ft.TapEvent): Evento de clique
    """

    if e.control.data != e.control.page.route:
        e.control.page.go(e.control.data)


def navbar_text_button(text: str, route: str, selected_route: str) -> ft.TextButton:
    """Componente de botão de texto da barra de navegação.

    Args:
        text (str): Texto do botão
        route (str): Rota para redirecionamento
        selected_route (str): Rota atual

    Returns:
        ft.TextButton: Componente de botão de texto
    """

    return ft.TextButton(
        text=text,
        data=route,
        on_click=handle_click,
        style=ft.ButtonStyle(
            color="white",
            text_style=ft.TextStyle(
                size=18,
                weight=ft.FontWeight.BOLD if selected_route == route else ft.FontWeight.NORMAL
            )
        )
    )


def navbar_icon_button(icon: ft.Icons, icon_selected: ft.Icons, route: str, selected_route: str) -> ft.IconButton:
    """Componente de botão de ícone da barra de navegação.

    Args:
        icon (ft.Icons): Ícone não selecionado
        icon_selected (ft.Icons): Ícone selecionado
        route (str): Rota para redirecionamento
        selected_route (str): Rota atual

    Returns:
        ft.IconButton: Componente de botão de ícone
    """

    return ft.IconButton(
        icon=icon_selected if selected_route == route else icon,
        icon_color="white",
        icon_size=22,
        data=route,
        on_click=handle_click
    )


def navbar(route: str) -> ft.Container:
    """Componente de navegação da aplicação.

    Args:
        route (str): Rota atual

    Returns:
        ft.Container: Componente de navegação.
    """

    return ft.Container(
        ft.Row([
            ft.Text("SPACE MANAGER", **styles["navbar-title"]),
            ft.Row(
                [
                    navbar_text_button("Reservas", "reservas", route),
                    navbar_text_button("Espaços", "espacos", route),
                    ft.Container(**styles["navbar-divider"]),
                    navbar_icon_button(ft.Icons.INFO_OUTLINE, ft.Icons.INFO, "sobre", route)
                ],
                **styles["navbar-nav"]
            )
        ], **styles["navbar-row"]),
        **styles["navbar-container"],
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

    "navbar-title": {
        "color": "white",
        "size": 30,
        "weight": ft.FontWeight.BOLD,
        "font_family": "Saira Extra Condensed - Bold"
    },

    "navbar-nav": {
        "vertical_alignment": ft.CrossAxisAlignment.CENTER,
        "spacing": 12
    },

    "navbar-divider": {
        "width": 0,
        "height": 24,
        "border": ft.border.all(1, "white")
    }
}
