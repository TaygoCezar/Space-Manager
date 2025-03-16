import flet as ft

# Validar dados
from utils.validate_espacos import validate_nome, validate_codigo

# Serviços
from services.espacos import get_by_codigo, update_espaco

#Componentes Personalizados
from components.navbar import navbar 
from components.form.button_filled import button_filled
from components.form.label import label
from components.form.input import input

def espacos_editar(page: ft.Page):
    codigo_ref = ft.Ref[str]()
    is_nome_valid, reset_nome, nome_input = input("Digite o nome do espaço", validate_nome)
    is_codigo_valid, reset_codigo, codigo_input = input("Digite o código do espaço", lambda codigo: validate_codigo(codigo, codigo_ref.current))

    def init(codigo):
        codigo_ref.current = codigo

        espaco = get_by_codigo(codigo)
        reset_nome(espaco["nome"])
        reset_codigo(espaco["codigo"])
        
        page.update()
    
    def handle_save(e):
        if not all([is_nome_valid(), is_codigo_valid()]):
            page.update()
            return
        
        update_espaco(codigo_ref.current, codigo_input.value, nome_input.value)
        page.open(ft.SnackBar(ft.Text("Edição do espaço salva com sucesso!"), duration=1000))
        init(codigo_input.value)
        
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

                    ft.Column([label("Nome"), nome_input], **styles["input-field-column"]),
                    ft.Column([label("Código"), codigo_input], **styles["input-field-column"]),
                    
                    ft.Row([button_filled("Salvar", ft.Icons.SAVE, handle_save)], **styles["right-row"])

                ], **styles["main-row"]),
                **styles["main-container"]
            )
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