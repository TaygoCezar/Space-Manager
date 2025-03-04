from flet import Page
from flet import View, Text

def home(page: Page) -> View:
    return View(
        "home",
        [
            Text("olá mundo")
        ]
    )