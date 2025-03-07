from flet import Ref
from flet import Page
from flet import View, Container, Row, Text
from flet import TextField
from flet import MainAxisAlignment, padding, FontWeight, border_radius, TextStyle, TextBaseline
from flet import Icon, Icons

def home(page: Page) -> View:
    busca_ref = Ref[TextField]()

    def handle_busca(e):
        print(busca_ref.current.value)

    return View(
        "home",
        [
            Container(
                Row(
                    [
                        Text("Space Manager", **styles["navigation-title"]),
                        Row(
                            [
                                Container(
                                    TextField(ref=busca_ref, on_change=handle_busca, **styles["navigation-search"]),
                                    **styles["navigation-search-container"]
                                ),
                                Text("|", size=35, color="#ffffff"),
                                Icon(Icons.MENU_ROUNDED, **styles["navigation-menu"])
                            ],
                            vertical_alignment=MainAxisAlignment.CENTER
                        )
                    ],
                    **styles["navigation-row"]
                ),
                **styles["navigation-container"]
            )   
        ],
        **styles["view"]
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
    },
    "navigation-title": {
        "font_family": "InstrumentSans-Bold",
        "size": 35,
        "weight": FontWeight.BOLD,
        "color": "#ffffff"
    },
    "navigation-search-container": {
        "width": 400,
        "height": 50,
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
    "navigation-menu": {
        "size": 40,
        "color": "#ffffff"
    }
}   





