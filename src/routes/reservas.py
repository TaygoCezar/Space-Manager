import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Componentes Personalizados
from components.navbar import navbar

def reservas():
    return ft.View(
        controls=[
            navbar("reservas"),
            ft.Container(
                ft.Column([
                    ft.Text("Reservas", **styles["header"]),
                    ft.Row([
                        ft.FilledButton("Adicionar Reserva", "add", **styles["filled-button"]),
                        ft.DropdownM2(
                            options=[
                                ft.DropdownOption("proximos","Mostrar próximos"),
                                ft.DropdownOption("todos", "Mostrar todos")                                
                            ],
                            value="proximos", **styles["dropdown"]
                        ),
                        ft.TextField(hint_text="Buscar", **styles["search"])
                        
                                 
                    ]), 
                ]),
                **styles["main-container"]
            )  
        ],
        **styles["body"]
    )






styles = {
    "body": {
        "padding": ft.padding.all(0),
    },
    
    "main-container": {
        "padding":ft.padding.symmetric(25,25) 
    },
    
    "main-row": {
    },
    
    "header": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Bold",
        "size": 25
    },
    
    "filled-button": {
        "bgcolor": "#003565",
        "style": ft.ButtonStyle(
            padding= ft.padding.symmetric(18, 20),
            shape=ft.RoundedRectangleBorder(9),
            text_style=ft.TextStyle(
                size=16
            )
        ),
        "height": 50
    },
    
    "dropdown": {
        "color": "#003565",
        
        "border_radius": 9,
        "border_color": "#003565",
        "border_width": 1.5,
        "height": 50,
        "width":200,
        "select_icon": ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, color="#003565"),
        "text_size": 16
    },
    
    "search": {
        "height": 50,
        "color": "#003565", 
        "border_color":"#003565", 
        "border_radius": 9, 
        "border_width": 1.5, 
        "suffix_icon": ft.Icon(ft.Icons.SEARCH, color="#003565"),
        "hint_style": ft.TextStyle(color="#4F7495")
    }

}