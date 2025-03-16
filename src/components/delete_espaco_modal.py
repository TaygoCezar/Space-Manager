import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Servicos
from services.espacos import delete_espaco

def delete_modal(codigo, page, callback):
    def handle_delete(e):
        delete_espaco(e.control.data)
        page.close(modal)
        callback()

    return ft.AlertDialog(
        modal=True,
        title=ft.Text("Deletar Reserva", **styles["title"]),
        content=ft.Column([
            ft.Text("Tem certeza que deseja deletar esta reserva?", **styles["description"]),
            ft.Text("(Esta ação também deletará todas as reservas cadastradas neste espaço!)", **styles["description-warning"])
        ], **styles["modal-column"]),
        actions=[
            ft.FilledButton("Cancelar", on_click=lambda e: page.close(modal), **styles["filled-button"]),
            ft.FilledButton("Deletar", data=codigo, on_click=handle_delete, **styles["filled-button"])
        ]
    )

def open_delete_modal(codigo: str, page: ft.Page, callback):
    global modal

    modal = delete_modal(codigo, page, callback)
    page.open(modal)

styles = {
    "modal-column": {
        "tight": True,
        "spacing": 0
    },
    "title": {
        "color": "#003565",
        "size": 22,
        "weight": "bold"
    },
    "description": {
        "color": "#003565",
        "size": 16
    },
    "description-warning": {
        "color": "#6A1414",
        "size": 14
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