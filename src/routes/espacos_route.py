import flet as ft

#controllers
from controllers.espacos_controller import get_espacos_by_key

# Componentes Personalizados
from components.navbar import navbar
from components.table.table import table
from components.espacos.espacos_table_row import espacos_table_row

def espacos(page: ft.Page):
    """Página Espaços
    
    Página com a lista de espaços cadastrados.

    Args:
        page (ft.Page): Página atual

    Returns:
        function: Função de inicialização
        ft.View: Página Espaços
    """
    # Referências
    search_ref = ft.Ref[ft.TextField]()

    # Inicialização
    def init():
        search_ref.current.value = ""
        update_table()

    # Eventos
    def add_espaco(e: ft.TapEvent):
        page.go("espacos_adicionar")

    def search_espacos(e: ft.ControlEvent):
        update_table()

    # Componentes
    update_table, table_component = table(
        page=page,
        get_data=get_espacos_by_key,
        get_data_parameters={"key": search_ref},
        columns=["CÓDIGO", "NOME", ""],
        row=espacos_table_row
    )

    return init, ft.View(
        controls=[
            navbar("espacos"),
            
            ft.Container(
                ft.Column([
                    ft.Text("Espaços", **styles["header"]),

                    # Controles
                    ft.Row([
                        ft.FilledButton("Adicionar Espaço", "add", on_click=add_espaco, **styles["filled-button"]),
                        ft.TextField(ref=search_ref, hint_text="Buscar", on_change=search_espacos, **styles["search"])
                    ]),
                    
                    table_component
                ]),
                **styles["main-container"]
            ),
            
        ],
        **styles["body"],
    )

# Estilos
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

