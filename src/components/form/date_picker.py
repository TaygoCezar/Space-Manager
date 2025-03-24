import typing as tp
from datetime import datetime as dt
import flet as ft

def date_picker(ref: ft.Ref|None = None, on_change_blur: tp.Callable = lambda: None) -> ft.TextField:
    """Componente de date picker.

    Args:
        ref (ft.Ref, optional): Referência do input. Defaults to None.
        handle (ft.EventHandler, optional): Função de mudança. Defaults to None.
        validate (function, optional): Função de validação. Defaults to lambda value: None.
    """
    # Referências
    input_ref = ft.Ref[ft.DatePicker]() if ref is None else ref

    # Funções
    def get_date():
        try:
            return dt.strptime(input_ref.current.value, "%d/%m/%Y")
        except:
            return dt.now()

    # Eventos
    def set_date(e):
        input_ref.current.value = e.control.value.strftime("%d/%m/%Y")
        handle_change_blur(e)

    def handle_change_blur(e: ft.ControlEvent):
        on_change_blur()
    
    # Componente
    return ft.TextField(
        ref=input_ref,
        hint_text="dd/mm/aaaa",
        suffix_icon=ft.Container(
            ft.Icon(ft.Icons.CALENDAR_TODAY, **styles["date-picker-icon"]),
            on_click=lambda e: e.control.page.open(ft.DatePicker(
                help_text="Selecione a data",
                value=get_date(),
                first_date=dt.now(),
                on_change=set_date
            ))
        ),
        on_blur=handle_change_blur,
        on_change=handle_change_blur,
        **styles["date-picker"]
    )


# Estilos
styles = {
    "date-picker": {
        "color": "#003565", 
        "border_color":"#003565", 
        "border_radius": 9, 
        "border_width": 1.5,
        "hint_style": ft.TextStyle(color="#4F7495")
    },
    "date-picker-icon": {
        "color": "#003565"
    }
}