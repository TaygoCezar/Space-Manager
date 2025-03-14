import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Controladores
from controllers.reservas import get_rows

# Componentes Personalizados
from components.navbar import navbar

def reservas(page: ft.Page):
    table_ref = ft.Ref[ft.DataTable]()

    dropdown_ref = ft.Ref[ft.DropdownM2]()
    search_ref = ft.Ref[ft.TextField]()

    def init():
        update_rows()

    def update_rows():
        table_ref.current.rows = get_rows(search_ref.current.value, dropdown_ref.current.value)
        page.update()

    return init, ft.View(
        controls=[
            navbar("reservas"),

            # Body
            ft.Container(
                ft.Column([
                    ft.Text("Reservas", **styles["header"]),

                    # Controles
                    ft.Row([
                        ft.FilledButton("Adicionar Reserva", "add", **styles["filled-button"]),
                        ft.DropdownM2(
                            ref=dropdown_ref,
                            options=[
                                ft.DropdownOption("next","Mostrar próximos"),
                                ft.DropdownOption("all", "Mostrar todos")                                
                            ],
                            value="next",
                            on_change=lambda e: update_rows(),
                            **styles["dropdown"]
                        ),
                        ft.TextField(ref=search_ref, hint_text="Buscar", on_change=lambda e: update_rows(), **styles["search"])
                    ]),

                    # Tabela
                    ft.DataTable(
                        ref=table_ref,
                        columns=[
                            ft.DataColumn(ft.Text("CÓDIDO DO ESPAÇO"), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text("ESPAÇO"), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text("DONO"),heading_row_alignment=ft.MainAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text("INÍCIO"),heading_row_alignment=ft.MainAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text("FIM"),heading_row_alignment=ft.MainAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text("ESTADO"),heading_row_alignment=ft.MainAxisAlignment.CENTER),
                            ft.DataColumn(ft.Text(""),heading_row_alignment=ft.MainAxisAlignment.CENTER)                       
                        ],
                        **styles["table"]
                    )
                ]),
                **styles["main-container"]
            ),
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
    },

    "table": {
        "width": float("inf"),
        "border": ft.border.all(1, "#E0E3E8"),
        
        # Estilos Header
        "heading_row_color": "#ECF0F3",
        "heading_text_style": ft.TextStyle(
            color="#556064",
            size=12,
            weight=ft.FontWeight.BOLD
        ),
        
        # Estilos Body
        "horizontal_lines": ft.BorderSide(
            color="#E0E3E8",
            width=1
        ),
        "data_text_style": ft.TextStyle(
            color="#959896",
            weight=ft.FontWeight.BOLD
        )
    }
}   