import typing as tp
import flet as ft

# Serviços
from services.espacos_service import Espaco

# Componentes Personalizados
from components.espacos.delete_espaco_modal import delete_espaco_modal


def espacos_table_row(espaco: Espaco, update_table: tp.Callable) -> ft.DataRow:
    """Linha da Tabela de Espaços.

    Args:
        espaco (Espaco): Dados do Espaço
        update_table (Callable): Função de atualização da tabela

    Returns:
        ft.DataRow: Linha da Tabela de Espaços
    """
    # Eventos
    def edit(e: ft.TapEvent):
        e.control.page.go("espacos_editar", codigo=e.control.key)

    def delete(e: ft.TapEvent):
        e.control.page.open(delete_espaco_modal(e.control.key, update_table))

    # Componente
    return ft.DataRow(
        cells=[
            ft.DataCell(ft.Row([ft.Text(espaco["codigo"])], **styles["data-cell-row"])),
            ft.DataCell(ft.Row([ft.Text(espaco["nome"])], **styles["data-cell-row"])),
            ft.DataCell(
                ft.Row([
                    ft.IconButton(ft.Icons.EDIT, tooltip="Editar", key=espaco["codigo"], on_click=edit),
                    ft.IconButton(ft.Icons.DELETE, tooltip="Deletar", key=espaco["codigo"], on_click=delete)
                ], **styles["data-cell-row"])
            )  
        ]

    )


# Estilos
styles = {
    "data-cell-row": {
        "alignment": ft.MainAxisAlignment.CENTER,
        "spacing": 0
    }
}