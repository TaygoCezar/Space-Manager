import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

import flet as ft

# Componentes Personalizados
from components.navbar import navbar

def sobre():
    def init():
        pass

    return init, ft.View(
        controls=[
            navbar("sobre"),

            # Body
            ft.Container(
                ft.Column([
                    ft.Column([
                        ft.Text("Sobre", **styles["header"]),
                        ft.Text("Space Manager é uma aplicação para gestão de espaços. Onde é possível cadastrar espaços e realizar reservas.", **styles["text"]),
                    ]),

                    ft.Column([
                        ft.Text("Requisitos", **styles["header"]),

                        ft.Text("Tela Principal", **styles["subheader"]),
                        ft.Column([
                            ft.Text("• Esta tela deve apresentar uma tabela com todos os espaços reservados.", **styles["text"]),
                            ft.Text("• A apresentação deve estar ordenada por data da mais recente para a mais distante.", **styles["text"]),
                            ft.Text("• Cada reserva deve ter as seguintes informações: código do espaço, nome do espaço, dono da reserva, data e hora início, data e hora fim.", **styles["text"]),
                            ft.Text("• Nesta tela deve ter uma ação para criar espaços que irá navegar para a Tela Novo Espaço.", **styles["text"]),
                            ft.Text("• Nesta tela deve ter uma ação para criar reserva que irá navegar para a Tela Nova Reserva.", **styles["text"]),
                            ft.Text("• Esta tela deve ter um campo de pesquisa que permitirá buscar por prefixo em qualquer campo. A pesquisa não deve considerar letras maiúsculas e acentos.", **styles["text"]),
                            ft.Text("• A tabela deve também apresentar uma coluna com as ações editar e remover. O link editar deve ir para uma tela de edição com as mesmas regras da tela de cadastro de reserva.", **styles["text"]),
                        ], **styles["bullet-list"]),

                        ft.Text("Tela Novo Espaço", **styles["subheader"]),
                        ft.Column([
                            ft.Text("• Esta tela deve ter os campos código e nome.", **styles["text"]),
                            ft.Text("• Os campos são obrigatórios.", **styles["text"]),
                            ft.Text("• O campo código deve ser único.", **styles["text"]),
                            ft.Text("• Esta tela deve ter uma ação para permitir voltar para a tela principal.", **styles["text"]),
                        ], **styles["bullet-list"]),

                        ft.Text("Tela Nova Reserva", **styles["subheader"]),
                        ft.Column([
                            ft.Text("• Esta tela deve ter os campos: Espaço, dono da reserva, data e hora início e data e hora fim.", **styles["text"]),
                            ft.Text("• A campo dono da reserva deve ser uma caixa de seleção para listar os espaços existentes.", **styles["text"]),
                            ft.Text("• O cadastro deve validar o início e fim, não permitindo data+hora fim menor que data+hora início.", **styles["text"]),
                            ft.Text("• Se a data inicio e fim for no mesmo dia, a reserva deve ser de no mínimo 30 minutos.", **styles["text"]),
                            ft.Text("• Não deve ser possível reservar espaço com conflito de horário.", **styles["text"]),
                            ft.Text("• Esta tela deve ter uma ação para permitir voltar para a tela principal.", **styles["text"]),
                        ], **styles["bullet-list"]),
                    ]),

                    ft.Column([
                        ft.Text("Integrantes", **styles["header"]),
                        ft.Row([
                            ft.Container(
                                ft.Image("images/murilo_henrique.png", tooltip="Murilo Henrique Conde da Luz\n202404940018", **styles["integrant"]),
                                **styles["integrant-container"]
                            ),
                            ft.Container(
                                ft.Image("images/nathielly_castro.png", tooltip="Nathielly Neves de Castro\n202404940042", **styles["integrant"]),
                                **styles["integrant-container"]
                            ),
                            ft.Container(
                                ft.Image("images/pedro_mendes.png", tooltip="Pedro da Silva Mendes\n202404940024", **styles["integrant"]),
                                **styles["integrant-container"]
                            ),
                            ft.Container(
                                ft.Image("images/taygo_cezar.jpeg", tooltip="Taygo Cezar Costa Pereira\n202404940011", **styles["integrant"]),
                                **styles["integrant-container"]
                            )
                        ])
                    ]),
                ], **styles["main-column"]),
                **styles["main-container"]
            ),
        ],
        **styles["body"]
    )

styles = {
    "body": {
        "padding": ft.padding.all(0),
        "scroll": ft.ScrollMode.AUTO,
    },

    "main-container": {
        "padding":ft.padding.symmetric(25,25),
    },

    "main-column": {
        "spacing": 15,
    },
    
    "header": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Bold",
        "size": 25
    },

    "subheader": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Regular",
        "size": 20
    },

    "text": {
        "color": "#003565"
    },

    "bullet-list": {
        "spacing": 0
    },

    "integrant-container": {
        "border": ft.border.all(2, "#003565"),
        "border_radius": 1000,
    },
    "integrant": {
        "width": 100,
        "height": 100,
        "border_radius": 1000,
    }
}