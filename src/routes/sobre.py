import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Componentes Personalizados
from components.navbar import navbar

def sobre():
    return ft.View(
        controls=[
            navbar("sobre")
        ],
        **styles["body"]
    )

styles = {
    "body": {
        "padding": ft.padding.all(0),
    }
}