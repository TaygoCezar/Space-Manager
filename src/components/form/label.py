import flet as ft

def label(text):
    return ft.Text(text, **styles["label"])

styles = {
    "label": {
        "color": "#003565",
        "weight": ft.FontWeight.BOLD
    }
}