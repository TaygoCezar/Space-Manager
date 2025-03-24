import flet as ft

# Serviços
from services.espacos_service import get_espaco_by_codigo, update_espaco

# Controllers
from controllers.espacos_controller import validate_nome, validate_codigo

# Utils
from utils.validation_util import validate_ref

#Componentes Personalizados
from components.navbar import navbar 
from components.form.button_filled import button_filled
from components.form.label import label
from components.form.input import input


def espacos_editar(page: ft.Page):
    """Página de editar espaço

    Página para editar um espaço existente.

    Args:
        page (ft.Page): Página atual

    Returns:
        function: Função de inicialização   
        ft.View: Página de editar espaço
    """
    # Inicialização
    def init(codigo: str):
        current_codigo_ref.current = codigo

        espaco = get_espaco_by_codigo(codigo)

        if espaco is None:
            page.go("espacos")
            page.open(ft.SnackBar(ft.Text("Espaço não encontrado."), duration=1000))
            return

        for ref, value in zip([codigo_ref, nome_ref], espaco.values()):
            ref.current.value = value
            ref.current.error_text = None
        
        page.update()

    # Referências
    current_codigo_ref = ft.Ref[str]()
    nome_ref = ft.Ref[ft.TextField]()
    codigo_ref = ft.Ref[ft.TextField]()

    # Validações
    check_nome = validate_ref([nome_ref], validate_nome, [nome_ref])
    check_codigo = validate_ref([codigo_ref], validate_codigo, [codigo_ref, current_codigo_ref])

    # Eventos
    def save(e: ft.TapEvent):
        """Salva o espaço
        """
        if not all([check_nome(), check_codigo()]):
            page.update()
            return
        
        update_espaco(current_codigo_ref.current, codigo_ref.current.value, nome_ref.current.value)
        page.open(ft.SnackBar(ft.Text("Edição do espaço salva com sucesso!"), duration=1000))
        init(codigo_ref.current.value)
    
    # Componentes
    return init, ft.View(
        controls=[
            navbar("espacos_editar"),
            ft.Container(
                ft.Column([
                    ft.Row([
                        ft.Container(
                            ft.Icon(ft.Icons.ARROW_BACK_OUTLINED, **styles["header-button"]),
                            on_click=lambda e: page.go("espacos")
                        ),
                        ft.Text("Editar Espaço", **styles["header"]),
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