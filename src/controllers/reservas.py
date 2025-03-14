import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

from utils.data import format_date, categorize_interval
from utils.search import ignore_case, ignore_accent_marks, prefix_check

def get_rows(filter_key: str, filter_mode: str) -> list:
    reservas = [
        {"id": "1", "codigo-espaco": "sala-01", "nome-espaco": "Sala 01", "dono": "Nathielly", "inicio": "2025-03-13 13:00", "fim": "2025-03-17 14:00"},
        {"id": "2", "codigo-espaco": "sala-02", "nome-espaco": "Sala 02", "dono": "Murilo", "inicio": "2025-03-11 14:00", "fim": "2025-03-11 15:00"},
        {"id": "3", "codigo-espaco": "sala-03", "nome-espaco": "Sala 03", "dono": "Predo", "inicio": "2025-03-11 15:00", "fim": "2025-03-11 16:00"},
        {"id": "4", "codigo-espaco": "sala-04", "nome-espaco": "Sala 04", "dono": "Talizo", "inicio": "2025-03-11 16:00", "fim": "2025-03-11 17:00"},
    ]

    rows = []
    statuses = {
        "gone": ("Finalizada", "#E0E3E8"),
        "on going": ("Em andamento", "#2B6AB1"),
        "scheduled": ("Agendada", "#2BA850"),
    }

    filter_key = ignore_case(filter_key)
    filter_key = ignore_accent_marks(filter_key)

    def filter_any(reserva):
        for value in reserva.values():
            value = ignore_case(value)
            value = ignore_accent_marks(value)

            if prefix_check(value, filter_key):
                return True
        return False

    for reserva in reservas:
        status = categorize_interval(reserva["inicio"], reserva["fim"])

        reserva["inicio"] = format_date(reserva["inicio"])
        reserva["fim"] = format_date(reserva["fim"])

        if not filter_any(reserva):
            continue

        if filter_mode == "next" and status == "gone":
            continue

        status_name, status_color = statuses[status]

        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Row([ft.Text(reserva["codigo-espaco"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["nome-espaco"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["dono"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["inicio"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["fim"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Icon(ft.Icons.CIRCLE, color=status_color, tooltip=status_name)], **styles["data-cell-row"])),
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(ft.Icons.EDIT),
                        ft.IconButton(ft.Icons.DELETE)
                    ], **styles["data-cell-row"])
                )  
            ],
        )

        rows.append(row)
    
    return rows

styles = {
    "data-cell-row": {
        "alignment": ft.MainAxisAlignment.CENTER,
        "spacing": 0
    }
}