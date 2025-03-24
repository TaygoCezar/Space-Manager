import typing as tp
import flet as ft

# Serviços
from services.reservas_service import Reserva

# Componentes Personalizados
from components.reservas.delete_reserva_modal import delete_reserva_modal


def reservas_table_row(reserva: Reserva, update_table: tp.Callable) -> ft.DataRow:
    """Linha da Tabela de Reservas.

    Args:
        data (Reserva): Dados da Reserva
        update_table (Callable): Função de atualização da tabela

    Returns:
        ft.DataRow: Linha da Tabela de Reservas
    """
    # Cores
    status_colors = {
        "Finalizada": "#E0E3E8",
        "Em andamento": "#2B6AB1",
        "Agendada": "#2BA850",
    }

    # Eventos
    def edit(e: ft.TapEvent):
        e.control.page.go("reservas_editar", codigo=e.control.key)

    def delete(e: ft.TapEvent):
        e.control.page.open(delete_reserva_modal(e.control.key, update_table))

    # Componente
    return ft.DataRow(
        cells=[
            ft.DataCell(ft.Row([ft.Text(reserva["codigo-espaco"])], **styles["data-cell-row"])),
            ft.DataCell(ft.Row([ft.Text(reserva["nome-espaco"])], **styles["data-cell-row"])),
            ft.DataCell(ft.Row([ft.Text(reserva["dono"])], **styles["data-cell-row"])),
            ft.DataCell(ft.Row([ft.Text(reserva["formatted-inicio"])], **styles["data-cell-row"])),
            ft.DataCell(ft.Row([ft.Text(reserva["formatted-fim"])], **styles["data-cell-row"])),
            ft.DataCell(ft.Row([ft.Icon(ft.Icons.CIRCLE, color=status_colors[reserva["status"]], tooltip=reserva["status"])], **styles["data-cell-row"])),
            ft.DataCell(
                ft.Row([
                    ft.IconButton(ft.Icons.EDIT, tooltip="Editar", key=reserva["codigo"], on_click=edit),
                    ft.IconButton(ft.Icons.DELETE, tooltip="Deletar", key=reserva["codigo"], on_click=delete)
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
