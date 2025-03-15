import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Controladores
from controllers.reservas import get_reservas, render_reservas

# Componentes Personalizados
from components.navbar import navbar
from components.table import table
from components.delete_modal import open_delete_modal

def reservas(page: ft.Page):
    dropdown_ref = ft.Ref[ft.DropdownM2]()
    search_ref = ft.Ref[ft.TextField]()

    goto_page, table_component = table(
        get_data=get_reservas,
        get_data_parameters={"key": search_ref, "mode": dropdown_ref},
        render_data=render_reservas,
        columns = [ "CÓDIGO DO ESPAÇO", "ESPAÇO", "DONO", "INÍCIO", "FIM", "ESTADO", ""],
        page=page,
        on_delete=lambda id: open_delete_modal(id, page, lambda: goto_page(0)),
    )

    def init():
        goto_page(0, False)

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
                            on_change=lambda e: goto_page(0),
                            **styles["dropdown"]
                        ),
                        ft.TextField(ref=search_ref, hint_text="Buscar", on_change=lambda e: goto_page(0), **styles["search"])
                    ]),

                    table_component
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
