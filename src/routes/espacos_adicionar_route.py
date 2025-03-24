import typing as tp
import flet as ft

<<<<<<< HEAD:src/routes/espacos_adicionar.py
from components.main import main

=======
# Serviços
from services.espacos_service import add_espaco

# Controllers
from controllers.espacos_controller import validate_nome, validate_codigo

# Utils
from utils.validation_util import validate_ref
>>>>>>> stable:src/routes/espacos_adicionar_route.py

def load(page: ft.Page) -> tuple:
    """Carrega a página de adicionar espaços.

<<<<<<< HEAD:src/routes/espacos_adicionar.py
    Args:
        page (ft.Page): Objeto da página.

    Returns:
        tuple: Nome da página, função de inicialização e view.
    """

    def handle_start() -> None:
        """Função executada ao iniciar a página.
        """

    return "espacos_adicionar", handle_start, main(
        "espacos_adicionar",
        "Adicionar Espaço",
        "espacos",
=======

def espacos_adicionar(page: ft.Page) -> tuple[tp.Callable, ft.View]:
    """Página de adicionar espaço

    Página para adicionar um novo espaço.

    Args:
        page (ft.Page): Página atual

    Returns:
        Callable: Função de inicialização
        ft.View: Página de adicionar espaço
    """
    # Inicialização
    def init():
        for ref in [nome_ref, codigo_ref]:
            ref.current.value = ""
            ref.current.error_text = None
        
        page.update()
    
    # Referências
    nome_ref = ft.Ref[ft.TextField]()
    codigo_ref = ft.Ref[ft.TextField]()

    # Validações
    check_nome = validate_ref([nome_ref], validate_nome, [nome_ref])
    check_codigo = validate_ref([codigo_ref], validate_codigo, [codigo_ref])
    
    # Eventos
    def save(e: ft.TapEvent):
        """Salva o espaço
        """
        if not all([check_nome(), check_codigo()]):
            page.update()
            return
        
        add_espaco(codigo_ref.current.value, nome_ref.current.value)
        page.open(ft.SnackBar(ft.Text("Espaço salvo com sucesso!"), duration=1000))
        init()

    # Componentes
    return init, ft.View(
>>>>>>> stable:src/routes/espacos_adicionar_route.py
        controls=[

<<<<<<< HEAD:src/routes/espacos_adicionar.py
        ]
    )


=======
                    ft.Column([label("Nome"), input("Digite o nome do espaço", nome_ref, check_nome)], **styles["input-field-column"]),
                    ft.Column([label("Código"), input("Digite o código do espaço", codigo_ref, check_codigo)], **styles["input-field-column"]),
                    
                    ft.Row([button_filled("Salvar", ft.Icons.SAVE, save)], **styles["right-row"])

                ], **styles["main-row"]),
                **styles["main-container"]
            )
        ],
        **styles["body"]
    )


# Estilos
>>>>>>> stable:src/routes/espacos_adicionar_route.py
styles = {

}