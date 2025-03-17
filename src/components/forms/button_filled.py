import flet as ft


def button_filled(text: str, icon: ft.Icons|None = None, on_click = None):
    """Botão com preenchimento.

    Args:
        text (str): Texto do botão.
        icon (ft.Icons|None, optional): Ícone do botão. Defaults to None.
        on_click (optional): Evento de clique do botão. Defaults to None.

    Returns:
        ft.FilledButton: Botão com preenchimento.
    """

    return ft.FilledButton(text, icon, on_click=on_click, **styles["filled-button"])


styles = {
    "filled-button": {
        "bgcolor": "#003565",
        "style": ft.ButtonStyle(
            padding= ft.padding.symmetric(18, 20),
            shape=ft.RoundedRectangleBorder(9),
            text_style=ft.TextStyle(
                size=16
            )
        )
    },
}