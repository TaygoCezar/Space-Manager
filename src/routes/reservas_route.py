import flet as ft

# Controladores
from controllers.reservas_controller import get_reservas_by_key_and_mode

# Componentes Personalizados
from components.navbar import navbar
from components.table.table import table
from components.reservas.reservas_table_row import reservas_table_row


def reservas(page: ft.Page):
    """Página Reservas

    Página com a lista de reservas cadastradas.

    Args:
        page (ft.Page): Página atual

    Returns:
        function: Função de inicialização
        ft.View: Página Reservas
    """
    # Referências
    dropdown_ref = ft.Ref[ft.DropdownM2]()
    search_ref = ft.Ref[ft.TextField]()

    # Inicialização
    def init():
        search_ref.current.value = ""
        dropdown_ref.current.value = "next"
        update_table()

    # Eventos
    def add_reserva(e: ft.TapEvent):
        page.go("reservas_adicionar")

    def search_reservas(e: ft.ControlEvent):
        update_table()

    # Componentes
    update_table, table_component = table(
        page=page,
        get_data=get_reservas_by_key_and_mode,
        get_data_parameters={"key": search_ref, "mode": dropdown_ref},
        columns=["CÓDIGO DO ESPAÇO", "ESPAÇO", "DONO", "INÍCIO", "FIM", "ESTADO", ""],
        row=reservas_table_row
    )

    return init, ft.View(
        controls=[
            navbar("reservas"),

            # Body
            ft.Container(
                ft.Column([
                    ft.Text("Reservas", **styles["header"]),

                    # Controles
                    ft.Row([
                        ft.FilledButton("Adicionar Reserva", "add", on_click=add_reserva, **styles["filled-button"]),
                        ft.DropdownM2(
                            ref=dropdown_ref,
                            options=[
                                ft.DropdownOption("next","Mostrar próximos"),
                                ft.DropdownOption("all", "Mostrar todos")                                
                            ],
                            value="next",
                            on_change=search_reservas,
                            **styles["dropdown"]
                        ),
                        ft.TextField(ref=search_ref, hint_text="Buscar", on_change=search_reservas, **styles["search"])
                    ]),

                    table_component
                ]),
                **styles["main-container"]
            ),
        ],
        **styles["body"]
    )


# Estilos
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
