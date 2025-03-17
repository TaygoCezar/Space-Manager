import flet as ft

from components.navigation.navbar import navbar


def main(route: str, header: str, back: str|None = None, controls: list[ft.Control] = []) -> ft.View:
    """Componente principal das páginas da aplicação.

    Args:
        route (str): Rota atual
        header (str): Título da página
        back (str|None, optional): Rota de retorno. Defaults to None.
        controls (list[ft.Control], optional): Lista de controles. Defaults to [].

    Returns:
        list: Lista de componentes
    """

    return ft.View(
        controls=[
            navbar(route),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        ft.Icon(ft.Icons.ARROW_BACK_OUTLINED, **styles["header-button"]),
                        on_click=lambda e: e.control.page.go(back),
                        visible=back is not None
                    ),
                    ft.Text(header, **styles["header"]),
                ]),

                *controls
            ]), **styles["main-container"])
        ],
        **styles["view"]
    )


styles = {
    "view": {
        "padding": ft.padding.all(0)
    },
    "main-container": {
        "padding":ft.padding.symmetric(25,25) 
    },

    "header-button": {
        "color": "#003565",
    },
    "header": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Bold",
        "size": 25
    },
}