import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Servicos
from services.reservas import delete_reserva

def delete_modal(id, page, callback):
    def handle_delete(e):
        delete_reserva(e.control.data)
        page.close(modal)
        callback()

    return ft.AlertDialog(
        modal=True,
        title=ft.Text("Deletar Reserva", **styles["title"]),
        content=ft.Text("Tem certeza que deseja deletar esta reserva?", **styles["description"]),
        actions=[
            ft.FilledButton("Cancelar", on_click=lambda e: page.close(modal), **styles["filled-button"]),
            ft.FilledButton("Deletar", data=id, on_click=handle_delete, **styles["filled-button"])
        ]
    )

def open_delete_modal(id: str, page: ft.Page, callback):
    global modal

    modal = delete_modal(id, page, callback)
    page.open(modal)

styles = {
    "title": {
        "color": "#003565",
        "size": 22,
        "weight": "bold"
    },
    "description": {
        "color": "#003565",
        "size": 16
    },
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