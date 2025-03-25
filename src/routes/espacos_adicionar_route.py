import typing as tp
import flet as ft

# Serviços
from services.espacos_service import add_espaco

# Controllers
from controllers.espacos_controller import validate_nome, validate_codigo

# Utils
from utils.validation_util import validate_ref

#Componentes Personalizados
from components.navbar import navbar 
from components.form.button_filled import button_filled
from components.form.label import label
from components.form.input import input


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
        controls=[
            navbar("espacos_adicionar"),
            ft.Container(
                ft.Column([
                    ft.Row([
                        ft.Container(
                            ft.Icon(ft.Icons.ARROW_BACK_OUTLINED, **styles["header-button"]),
                            on_click=lambda e: page.go("espacos")
                        ),
                        ft.Text("Adicionar Espaço", **styles["header"]),
                    ]),

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
styles = {
    "body": {
        "padding": ft.padding.all(0),
    },
    "main-container": {
        "padding":ft.padding.symmetric(25,25) 
    },
    
    "main-row": {
        "spacing": 20
    },
    
    "header": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Bold",
        "size": 25
    },
    
    "header-button": {
        "color": "#003565",
    },
    
    "input-field-column": {
        "spacing": 5
    },
    
    "right-row": {
        "alignment": ft.MainAxisAlignment.END
    }
}