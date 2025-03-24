import flet as ft

<<<<<<< HEAD:src/routes/espacos.py
from components.main import main
from components.forms.button_filled import button_filled


def load(page: ft.Page) -> tuple:
    """Carrega a página de espaços.

    Args:
        page (ft.Page): Objeto da página.

    Returns:
        tuple: Nome da página, função de inicialização e view.
    """
=======
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
>>>>>>> stable:src/routes/espacos_route.py

    def handle_start() -> None:
        """Função executada ao iniciar a página.
        """

    return "espacos", handle_start, main(
        "espacos",
        "Espaços",
        controls=[
<<<<<<< HEAD:src/routes/espacos.py
            ft.Row([
                button_filled("Adicionar Espaco", "add", lambda e: e.control.page.go("espacos_adicionar")),
            ])
        ]
    )


=======
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
>>>>>>> stable:src/routes/espacos_route.py
styles = {

}