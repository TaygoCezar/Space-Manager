import flet as ft

def input(hint, validate, validate_params={}):
    input_ref = ft.Ref[ft.TextField]()

    def is_valid():
        error = validate(input_ref.current.value, **validate_params)
        input_ref.current.error_text = error
        return error is None

    def reset(value=""):
        input_ref.current.value = value
        input_ref.current.error_text = None

    def handle_input(e):
        is_valid()
        e.control.page.update()

    return is_valid, reset, ft.TextField(
        ref=input_ref,
        hint_text=hint,
        on_blur=handle_input,
        on_change=handle_input,
        **styles["input"]
    )

styles = {
    "input": {
        "color": "#003565", 
        "border_color":"#003565", 
        "border_radius": 9, 
        "border_width": 1.5,
        "hint_style": ft.TextStyle(color="#4F7495")
    }
}