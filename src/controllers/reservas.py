import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft
import math
from datetime import datetime as dt

from utils.data import format_date, categorize_interval
from utils.search import prefix_check

from services.reservas import get_all

def categorize_intervals(reservas: list) -> list:
    def f(reserva):
        reserva["status"] = categorize_interval(reserva["inicio"], reserva["fim"]) # -> "gone", "on going", "scheduled"
        return reserva

    return list(map(f, reservas))


def sort_reservas(reservas: list) -> list:
    now = dt.now()

    def f(reserva):
        return abs(dt.strptime(reserva["inicio"], "%Y-%m-%d %H:%M") - now)
    
    reservas.sort(key=f)
    return reservas


def format_dates(reservas: list) -> list:
    def f(reserva): 
        reserva["inicio"] = format_date(reserva["inicio"])
        reserva["fim"] = format_date(reserva["fim"])
        return reserva
    
    return list(map(f, reservas))


def search(reservas: list, key: str) -> list:
    def f(reserva: dict) -> bool:
        for value in reserva.values():
            if prefix_check(value, key): 
                return True
        return False

    return list(filter(f, reservas))


def select(reservas: list, mode: str) -> list:
    if mode == "all":
        return reservas
    
    def f(reserva: dict) -> bool:
        return reserva["status"] != "Finalizada"
    
    return list(filter(f, reservas))

def get_reservas(key: str, mode: str) -> list:
    # Carregar dados
    reservas = get_all()

    reservas = categorize_intervals(reservas) # Cria o campos "status"
    reservas = sort_reservas(reservas)
    reservas = format_dates(reservas) # Transforma as datas em strings formatadas
    reservas = search(reservas, key) # Filtra as reservas com base no campo de busca
    reservas = select(reservas, mode) # Filtra as reservas com base no modo de visualização selecionado

    return reservas

def render_reservas(reservas, number_of_page, rows_per_page, on_edit, on_delete) -> list:
    status_colors = {
        "Finalizada": "#E0E3E8",
        "Em andamento": "#2B6AB1",
        "Agendada": "#2BA850",
    }

    start = number_of_page * rows_per_page
    end = start + rows_per_page

    return [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Row([ft.Text(reserva["codigo-espaco"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["nome-espaco"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["dono"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["inicio"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Text(reserva["fim"])], **styles["data-cell-row"])),
                ft.DataCell(ft.Row([ft.Icon(ft.Icons.CIRCLE, color=status_colors[reserva["status"]], tooltip=reserva["status"])], **styles["data-cell-row"])),
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(ft.Icons.EDIT, key=reserva["id"], on_click=lambda e: on_edit(e.control.key)),
                        ft.IconButton(ft.Icons.DELETE, key=reserva["id"], on_click=lambda e: on_delete(e.control.key))
                    ], **styles["data-cell-row"])
                )  
            ]
        )
        for reserva in reservas[start:end]
    ]

styles = {
    "data-cell-row": {
        "alignment": ft.MainAxisAlignment.CENTER,
        "spacing": 0
    }
}
