from flet import app
from flet import Page

import router

def main(page: Page) -> None:
    router.init(page)
    page.on_route_change = router.navigate
    page.go("home")

if __name__ == "__main__":
    app(target=main)