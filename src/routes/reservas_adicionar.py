import flet as ft

# Componentes Personalizados
from components.navbar import navbar

def reservas_adicionar(page):
    def init():
        pass

    return init, ft.View(
        controls=[
            navbar("reservas_adicionar"),
            ft.Container(
                ft.Column([
                    ft.Row([
                        ft.Container(
                            ft.Icon(ft.Icons.ARROW_BACK_OUTLINED, **styles["header-button"]),
                            on_click=lambda e: page.go("reservas")
                        ),
                        ft.Text("Adicionar Reserva", **styles["header"]),
                    ]),

                    ft.Column([
                        ft.Text("Dono", **styles["label"]),
                        ft.TextField(hint_text="Digite o nome do responsável pela reserva", **styles["input"])
                    ], **styles["input-field-column"]),

                    ft.Column([
                        ft.Text("Espaço", **styles["label"]),
                        ft.Dropdown (hint_text="Selecione o espaço", **styles["select"])
                    ], **styles["input-field-column"]),

                    ft.Row([
                        ft.Row([
                            ft.Column([
                                ft.Text("Data de Início", **styles["label"]),
                                ft.TextField(hint_text="dd/mm/aaaa", **styles["input"])
                            ], **styles["input-field-column"]),
                            ft.Column([
                                ft.Text("Horário de Início", **styles["label"]),
                                ft.TextField(hint_text="hh:mm", **styles["input"])
                            ], **styles["input-field-column"])
                        ]),

                        ft.Row([
                            ft.Column([
                                ft.Text("Data de Fim", **styles["label"]),
                                ft.TextField(hint_text="dd/mm/aaaa", **styles["input"])
                            ], **styles["input-field-column"]),
                            ft.Column([
                                ft.Text("Horário de Fim", **styles["label"]),
                                ft.TextField(hint_text="hh:mm", **styles["input"])
                            ], **styles["input-field-column"])
                        ]), 
                    ]),

                    ft.Row([
                        ft.FilledButton("Salvar", ft.Icons.SAVE)
                    ])
                    
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

    "header-button": {
        "color": "#003565",
    },

    "header": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Bold",
        "size": 25
    },

    "input-field-column": {
        "spacing": 5
    },

    "input": {
        "height": 50,
        "color": "#003565", 
        "border_color":"#003565", 
        "border_radius": 9, 
        "border_width": 1.5,
        "hint_style": ft.TextStyle(color="#4F7495")
    },

    "select": {
        "color": "#003565",
        "border_radius": 9,
        "border_color": "#003565",
        "border_width": 1.5,
        "height": 50,
        "select_icon": ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, color="#003565"),
        "text_size": 16,
        "hint_style": ft.TextStyle(color="#4F7495")
    },

    "label": {
        "color": "#003565",
        "weight": ft.FontWeight.BOLD
    }
}