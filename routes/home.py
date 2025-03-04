from flet import Page
from flet import View, Container, Row, Text
from flet import padding, FontWeight

def home(page: Page) -> View:
    return View(
        "home",
        [
            Container(
                Row([
                    Text("Space Manager", **styles["navigation-title"])
                ]),
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
        "padding": padding.symmetric(20, 40),
        "bgcolor": "#98D4C6",
    },
    "navigation-title": {
        "font_family": "InstrumentSans-Bold",
        "size": 35,
        "weight": FontWeight.BOLD,
        "color": "#ffffff"
    }
}