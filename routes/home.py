import sys
sys.path.insert(0, r"C:\Users\taygo\Downloads\PASTA DE TESTE\services")

from reservas import get_all as get_all_reservas
from espacos import get_all as get_all_espacos

from datetime import datetime

from flet import Ref
from flet import Page
from flet import View, Container, Column, Row, Text
from flet import TextField
from flet import IconButton
from flet import DataTable, DataColumn, DataRow, DataCell
from flet import MainAxisAlignment, CrossAxisAlignment, padding, margin, FontWeight, border, border_radius, TextStyle, ScrollMode, ClipBehavior, BorderSide
from flet import Icon, Icons

from flet import NavigationDrawer, NavigationDrawerDestination, NavigationDrawerPosition
from flet import ContinuousRectangleBorder

def carregar_reservas():
    espacos = get_all_espacos()
    reservas = get_all_reservas()

    data_atual = datetime.now()

    reservas = [reserva for reserva in reservas if datetime.strptime(reserva["datah-inicio"], "%Y-%m-%d %H:%M") >= data_atual]
    reservas.sort(key=lambda reserva: abs(data_atual - datetime.strptime(reserva["datah-inicio"], "%Y-%m-%d %H:%M")))

    linhas = []

    for i, reserva in enumerate(reservas):
        nome_espaco = ""

        for espaco in espacos:
            if espaco["codigo"] == reserva["codigo-espaco"]:
                nome_espaco = espaco["nome"]
                break

        linha = DataRow([
            DataCell(Text(nome_espaco)),
            DataCell(Text(reserva["dono-reserva"])),
            DataCell(Text(reserva["datah-inicio"])),
            DataCell(Text(reserva["datah-fim"]))
        ], color="#DFF5F4" if i % 2 == 0 else "#C3EEEB")
        linhas.append(linha)

    return linhas

def home(page: Page) -> View:
    end_drawer_ref = Ref[NavigationDrawer]()
    busca_ref = Ref[TextField]()

    linhas = carregar_reservas()

    def handle_busca(e):
        print(busca_ref.current.value)

    def handle_open_drawer(e):
        page.open(end_drawer_ref.current)

    return View(
        "home",
        [
            Container(
                Row(
                    [
                        Text("SPACE MANAGER", **styles["navigation-title"]),

                        Row(
                            [
                                Container(
                                    TextField(ref=busca_ref, on_change=handle_busca, **styles["navigation-search"]),
                                    **styles["navigation-search-container"]
                                ),
                                Container(**styles["vertical-divider"]),
                                IconButton(
                                    Icons.MENU_ROUNDED,
                                    **styles["navigation-menu"],
                                    on_click=handle_open_drawer
                                ),
                            ],
                            **styles["navigation-right"]
                        )
                    ],
                    **styles["navigation-row"]
                ),
                **styles["navigation-container"]
            ),

            Container(
                Column([
                    Text("Reservas", **styles["main-title"]),
                    Container(
                        Column(
                            [
                                DataTable(
                                    columns=[
                                        DataColumn(Text("Espaço")),
                                        DataColumn(Text("Dono da Reserva")),
                                        DataColumn(Text("Data Início")),
                                        DataColumn(Text("Data Fim"))
                                    ],
                                    rows=linhas,
                                    **styles["table"]
                                )
                            ],
                            **styles["table-column"]
                        ),
                        **styles["table-container"]
                    )
                ]),
                **styles["main-container"]
            )
        ],
        **styles["view"],
        end_drawer=NavigationDrawer(
            ref=end_drawer_ref,
            position=NavigationDrawerPosition.END,
            controls=[
                NavigationDrawerDestination(icon=Icons.HOME, label="Home"),
                NavigationDrawerDestination(icon=Icons.ADD, label="Adicionar Espaço"),
                NavigationDrawerDestination(icon=Icons.ADD, label="Adicionar Reserva")
            ],
            indicator_shape=ContinuousRectangleBorder(),
            tile_padding=padding.all(0)
        )
    )

styles = {
    "view": {
        "bgcolor": "#FAF2F2",
        "padding": padding.all(0)
    },

    "navigation-container": {
        "padding": padding.symmetric(20, 70),
        "bgcolor": "#98D4C6",
    },
    "navigation-row": {
        "alignment": MainAxisAlignment.SPACE_BETWEEN,
        "vertical_alignment": CrossAxisAlignment.CENTER
    },

    "navigation-right": {
        "spacing": 20
    },

    "navigation-title": {
        "font_family": "InstrumentSans-Bold",
        "size": 35,
        "weight": FontWeight.BOLD,
        "style": TextStyle(height=1),
        "color": "#ffffff"
    },

    "navigation-search-container": {
        "width": 400,
        "height": 50,

        "margin": margin.all(0)
    },
    "navigation-search": {        
        "fill_color": "#F0F0F0",
        "color": "#9E8F8F",
        
        "hint_text":"Buscar",
        "hint_style": TextStyle(color="#9E8F8F"),

        "border_radius": border_radius.all(50),
        "border_color": "#B6AEAE",
        "border_width": 0,

        "focused_bgcolor": "#CCCACA",   

        "suffix_icon": Icon(name=Icons.SEARCH, color="#B6AEAE")
    },

    "vertical-divider": {
        "height": 40,

        "border": border.all(1,"#ffffff"),
        "border_radius": border_radius.all(50)
    },

    "navigation-menu-container": {
        "ink": True
    },

    "navigation-menu": {
        "icon_size": 40,
        "icon_color": "#ffffff"
    },

    "main-container": {
        "padding": padding.symmetric(20, 70),
    },

    "main-title": {
        "color": "#6FB5A5",
        "size": 30,
        "weight": FontWeight.BOLD
    },

    "table-container": {
        "border_radius": border_radius.all(20),
        "clip_behavior": ClipBehavior.NONE
    },
    "table-column": {
        "height": 400,
        "scroll": ScrollMode.ADAPTIVE
    },
    "table": {
        "width": 2000,
        "bgcolor": "#C3EEEB",
        "border_radius": border_radius.all(20),

        "divider_thickness": 0,

        "heading_text_style": TextStyle(color="#2BA88A", weight=FontWeight.BOLD),
        "data_text_style": TextStyle(color="#2BA88A"),
    }
}   





