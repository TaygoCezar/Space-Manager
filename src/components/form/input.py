import typing as tp
import flet as ft


def input(hint: str, ref: ft.Ref|None = None, on_change_blur: tp.Callable = lambda: None) -> ft.TextField:
    """Componente de input.

    Args:
        hint (str): Texto de dica.
        ref (ft.Ref, optional): Referência do input. Defaults to None.
        on_change_blur (tp.Callable, optional): Função de mudança. Defaults to lambda: None.

    Returns:
        ft.TextField: Input.
    """
    # Referências
    input_ref = ft.Ref[ft.TextField]() if ref is None else ref

    # Eventos
    def handle_change_blur(e: ft.ControlEvent):
        on_change_blur()

    # Componente
    return ft.TextField(
        ref=input_ref,
        hint_text=hint,
        on_blur=handle_change_blur,
        on_change=handle_change_blur,
        **styles["input"]
    )


# Estilos
styles = {
    "input": {
        "color": "#003565", 
        "border_color":"#003565", 
        "border_radius": 9, 
        "border_width": 1.5,
        "hint_style": ft.TextStyle(color="#4F7495")
    }
}