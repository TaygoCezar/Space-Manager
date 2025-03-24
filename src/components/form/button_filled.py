import typing as tp
import flet as ft


def button_filled(text: str, icon: ft.Icons|None=None, on_click: tp.Callable=None) -> ft.FilledButton:
    """Componente de botão preenchido.

    Args:
        text (str): Texto do botão.
        icon (ft.Icons, optional): Ícone do botão. Defaults to None.
        on_click (tp.Callable, optional): Função de clique. Defaults to None.
    
    Returns:
        ft.FilledButton: Botão preenchido.
    """
    return ft.FilledButton(text, icon, **styles["filled-button"], on_click=on_click)


# Estilos
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