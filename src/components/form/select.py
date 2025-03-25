import typing as td
import flet as ft


def select(hint: str, ref: ft.Ref|None = None, on_change_blur: td.Callable = lambda: None) -> ft.DropdownM2:
    """Componente de select.

    Args:
        hint (str): Texto de dica.
        ref (ft.Ref, optional): Referência do select. Defaults to None.
        on_change (td.Callable, optional): Função de mudança. Defaults to lambda: None.

    Returns:
        ft.DropdownM2: Select.
    """
    # Referências
    dropdown_ref = ft.Ref[ft.DropdownM2]() if ref is None else ref

    # Eventos
    def handle_input(e: ft.ControlEvent):
        on_change_blur()

    return ft.DropdownM2(
        ref=dropdown_ref,
        hint_content=ft.Text(hint, **styles["select-hint"]),
        on_blur=handle_input,
        on_change=handle_input,
        **styles["select"]
    )


# Estilos
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