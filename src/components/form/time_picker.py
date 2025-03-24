import typing as tp
from datetime import datetime as dt
import flet as ft

def time_picker(ref: ft.Ref|None = None, on_change_blur: tp.Callable = lambda: None) -> ft.TextField:
    """Componente de time picker.

    Args:
        ref (ft.Ref, optional): Referência do input. Defaults to None.
        handle (ft.EventHandler, optional): Função de mudança. Defaults to None.
        validate (function, optional): Função de validação. Defaults to lambda value: None.
    """
    # Referências
    input_ref = ft.Ref[ft.TimePicker]() if ref is None else ref
    
    # Funções
    def get_time():
        try:
            return dt.strptime(input_ref.current.value, "%H:%M")
        except:
            return dt.now().time()

    # Eventos
    def set_time(e):
        input_ref.current.value = e.control.value.strftime("%H:%M")
        handle_input(e)

    def handle_input(e):
        on_change_blur()

    # Componente
    return ft.TextField(
        ref=input_ref,
        hint_text="hh:mm",
        suffix_icon=ft.Container(
            ft.Icon(ft.Icons.ACCESS_TIME, **styles["time-picker-icon"]),
            on_click=lambda e: e.control.page.open(ft.TimePicker(
                help_text="Selecione o horário",
                value=get_time(),
                on_change=set_time
            ))
        ),
        on_blur=handle_input,
        on_change=handle_input,
        **styles["time-picker"]
    )


# Estilos
styles = {
    "time-picker": {
        "color": "#003565", 
        "border_color":"#003565", 
        "border_radius": 9, 
        "border_width": 1.5,
        "hint_style": ft.TextStyle(color="#4F7495")
    },
    "time-picker-icon": {
        "color": "#003565"
    }
}