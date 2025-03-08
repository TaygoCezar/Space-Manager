from flet import Ref
from flet import Page
from flet import View, Container, Row, Text
from flet import TextField
from flet import MainAxisAlignment, CrossAxisAlignment, padding, margin, FontWeight, border, border_radius, TextStyle
from flet import Icon, Icons

from flet import NavigationDrawer, NavigationDrawerDestination, NavigationDrawerPosition
from flet import ContinuousRectangleBorder

def home(page: Page) -> View:
    end_drawer_ref = Ref[NavigationDrawer]()
    busca_ref = Ref[TextField]()

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

                        Container(
                            TextField(ref=busca_ref, on_change=handle_busca, **styles["navigation-search"]),
                            **styles["navigation-search-container"]
                        ),
                        # Row(
                        #     [
                        #         # Container(**styles["vertical-divider"]),
                        #         # Container(
                        #         #     Icon(Icons.MENU_ROUNDED, **styles["navigation-menu"]),
                        #         #     on_click=handle_open_drawer,
                        #         #     **styles["navigation-menu-container"]
                        #         # )
                        #     ],
                        #     **styles["navigation-right"]
                        # )
                    ],
                    **styles["navigation-row"]
                ),
                **styles["navigation-container"]
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
        "size": 40,
        "color": "#ffffff"
    }
}   





