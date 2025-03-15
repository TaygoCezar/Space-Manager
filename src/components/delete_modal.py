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
        title=ft.Text("Deletar Reserva"),
        content=ft.Text("Tem certeza que deseja deletar esta reserva?"),
        actions=[
            ft.FilledButton("Cancelar", on_click=lambda e: page.close(delete_modal)),
            ft.FilledButton("Deletar", data=id, on_click=handle_delete)
        ]
    )

def open_delete_modal(id: str, page: ft.Page, callback):
    global modal

    modal = delete_modal(id, page, callback)
    page.open(modal)
