import flet as ft

from services.espacos import get_all

from utils.search import prefix_check

def search(espacos: list, key: str) -> list:
    
    def f(espaco: dict) -> bool:
        for values in espaco.values():
            if prefix_check(values, key):
                return True
        return False
        
    return list(filter(f, espacos))

def get_espacos(key: str) -> list:
    espacos = get_all()

    espacos = search(espacos, key)

    return espacos

def render_espacos(espacos: list[dict], number_page, rows_per_page, on_edit, on_delete) -> list[ft.DataRow]:
    start = number_page * rows_per_page
    end = start + rows_per_page

    return [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Row([ft.Text(espaco["codigo"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(espaco["nome"])], **styles["data-cell-row"])),
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(ft.Icons.EDIT, tooltip="Editar", key=espaco["codigo"], on_click=lambda e: on_edit(e.control.key)),
                        ft.IconButton(ft.Icons.DELETE, tooltip="Deletar", key=espaco["codigo"], on_click=lambda e: on_delete(e.control.key))
                    ], **styles["data-cell-row"])
                )  
            ]

        )
        for espaco in espacos[start:end]
    ]

styles = {
    "data-cell-row": {
        "alignment": ft.MainAxisAlignment.CENTER,
        "spacing": 0
    }
}