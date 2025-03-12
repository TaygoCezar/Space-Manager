import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Componentes Personalizados
from components.navbar import navbar

def espacos():
    return ft.View(
        controls=[
            navbar("espacos")
        ],
        **styles["body"]
    )

styles = {
    "body": {
        "padding": ft.padding.all(0),
    }
}