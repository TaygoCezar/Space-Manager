import flet as ft
from datetime import datetime as dt

def date_picker(validate, handle=None):
    date_picker_ref = ft.Ref[ft.DatePicker]()
    
    def is_valid():
        error = validate(date_picker_ref.current.value)
        date_picker_ref.current.error_text = error
        return error is None
    
    def reset(value=""):
        date_picker_ref.current.value = value
        date_picker_ref.current.error_text = None

    def set_date(e):
        date_picker_ref.current.value = e.control.value.strftime("%d/%m/%Y")
        handle_input(e)

    def handle_input(e):
        if handle is not None:
            handle(e)
        else:
            is_valid()
        e.control.page.update()
    
    return is_valid, reset, ft.TextField(
        ref=date_picker_ref,
        hint_text="dd/mm/aaaa",
        suffix_icon=ft.Container(
            ft.Icon(ft.Icons.CALENDAR_TODAY, **styles["date-picker-icon"]),
            on_click=lambda e: e.control.page.open(ft.DatePicker(
                help_text="Selecione a data",
                value=dt.strptime(date_picker_ref.current.value, "%d/%m/%Y") if validate(date_picker_ref.current.value) is None else dt.now(),
                first_date=dt.now(),
                on_change=set_date
            ))
        ),
        on_blur=handle_input,
        on_change=handle_input,
        **styles["date-picker"]
    )

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