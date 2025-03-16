import flet as ft

def button_filled(text, icon =None, on_click=None):
    return ft.FilledButton(text, icon, **styles["filled-button"], on_click=on_click)

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