import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

#controllers
from controllers.espacos import get_espacos, render_espacos

# Componentes Personalizados
from components.navbar import navbar
from components.table import table
from components.delete_espaco_modal import open_delete_modal

def espacos(page: ft.Page):
    search_ref = ft.Ref[ft.TextField]()

    def init():
        search_ref.current.value = ""
        goto_page(0, False)

    goto_page, table_component = table(
        get_data=get_espacos,
        get_data_parameters={"key": search_ref},
        render_data=render_espacos,
        columns = ["CÓDIGO", "NOME", ""],
        page=page,
        on_edit=lambda codigo: page.go(f"espacos_editar", codigo=codigo),
        on_delete=lambda codigo: open_delete_modal(codigo, page, lambda: goto_page(0)),
    )

    return init, ft.View(
        controls=[
            navbar("espacos"),
            
            ft.Container(
                ft.Column([
                    ft.Text("Espaços", **styles["header"]),

                    # Controles
                    ft.Row([
                        ft.FilledButton("Adicionar Espaço", "add", on_click=lambda e: page.go("espacos_adicionar"), **styles["filled-button"]),
                        ft.TextField(ref=search_ref, hint_text="Buscar", on_change=lambda e: goto_page(0), **styles["search"])
                    ]),
                    
                    table_component
                ]),
                **styles["main-container"]
            ),
            
        ],
        **styles["body"],
    )

styles = {
    "body": {
        "padding": ft.padding.all(0),
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

    "search": {
        "height": 50,
        "color": "#003565", 
        "border_color":"#003565", 
        "border_radius": 9, 
        "border_width": 1.5, 
        "suffix_icon": ft.Icon(ft.Icons.SEARCH, color="#003565"),
        "hint_style": ft.TextStyle(color="#4F7495")
    },

    "main-container": {
        "padding":ft.padding.symmetric(25,25) 
    },
    
    "header": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Bold",
        "size": 25
    }
}

