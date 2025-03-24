import flet as ft


def label(text: str) -> ft.Text:
    """Cria a label de um formulário.
    
    Args:
        text (str): Texto da label.
    """
    return ft.Text(text, **styles["label"])


# Estilos
styles = {
    "label": {
        "color": "#003565",
        "weight": ft.FontWeight.BOLD
    }
}