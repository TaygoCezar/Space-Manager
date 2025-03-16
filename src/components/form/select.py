import flet as ft

def select(hint, render_options, validate, handle=None):
    dropdown_ref = ft.Ref[ft.DropdownM2]()

    def is_valid():
        error = validate(dropdown_ref.current.value)
        dropdown_ref.current.error_text = error
        return error is None
    
    def reset(value=""):
        dropdown_ref.current.value = value
        dropdown_ref.current.error_text = None
        dropdown_ref.current.options = render_options()

    def handle_input(e):
        is_valid()
        if handle:
            handle(e)
        e.control.page.update()
        
    return is_valid, reset, ft.DropdownM2(
        ref=dropdown_ref,
        hint_content=ft.Text(hint, **styles["select-hint"]),
        on_blur=handle_input,
        on_change=handle_input,
        **styles["select"]
    )

styles = {
    "select": {
        "width": float("inf"),
        "color": "#003565",
        "border_radius": 9,
        "border_color": "#003565",
        "border_width": 1.5,
        "select_icon": ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, color="#003565"),
        "text_size": 16,
    },
    "select-hint": {
        "color": "#4F7495"
    },
}