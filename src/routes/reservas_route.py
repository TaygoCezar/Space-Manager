import flet as ft

<<<<<<< HEAD:src/routes/reservas.py
from components.main import main


def load(page: ft.Page) -> tuple:
    """Carrega a página de reservas.

    Args:
        page (ft.Page): Objeto da página.

    Returns:
        tuple: Nome da página, função de inicialização e view.
    """
=======
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
>>>>>>> stable:src/routes/reservas_route.py

    def handle_start() -> None:
        """Função executada ao iniciar a página.
        """

    return "reservas", handle_start, main(
        "reservas",
        "Reservas",
        controls=[

<<<<<<< HEAD:src/routes/reservas.py
        ]
    )


=======
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
>>>>>>> stable:src/routes/reservas_route.py
styles = {

}