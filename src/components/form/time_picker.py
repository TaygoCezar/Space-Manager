import flet as ft
from datetime import datetime as dt

def time_picker(validate, handle=None):
    time_picker_ref = ft.Ref[ft.TimePicker]()
    
    def is_valid():
        error = validate(time_picker_ref.current.value)
        time_picker_ref.current.error_text = error
        return error is None
    
    def reset(value=""):
        time_picker_ref.current.value = value
        time_picker_ref.current.error_text = None

    def set_time(e):
        time_picker_ref.current.value = e.control.value.strftime("%H:%M")
        handle_input(e)

    def handle_input(e):
        if handle is not None:
            handle(e)
        else:
            is_valid()
        e.control.page.update()

    return is_valid, reset, ft.TextField(
        ref=time_picker_ref,
        hint_text="hh:mm",
        suffix_icon=ft.Container(
            ft.Icon(ft.Icons.ACCESS_TIME, **styles["time-picker-icon"]),
            on_click=lambda e: e.control.page.open(ft.TimePicker(
                help_text="Selecione o horário",
                value=dt.strptime(time_picker_ref.current.value, "%H:%M") if validate(time_picker_ref.current.value) is None else dt.now(),
                on_change=set_time
            ))
        ),
        on_blur=handle_input,
        on_change=handle_input,
        **styles["time-picker"]
    )

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