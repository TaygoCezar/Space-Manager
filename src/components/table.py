import flet as ft
import math

rows_per_page = 8

def get_number_of_pages(data):
    number_of_rows = len(data)
    return max(1, math.ceil(number_of_rows / rows_per_page))

def render_pages(data):
    number_of_pages = get_number_of_pages(data)

    return [
        ft.Container(ft.Text(i+1, **styles["pagination-text"]), key=i, bgcolor="#E1E1E1" if i == page_number_ref.current else "transparent", on_click=lambda e: goto(e.control.key), **styles["pagination-button"])
        for i in range(number_of_pages)
    ]

def table(get_data, get_data_parameters, render_data, columns: list, page: ft.Page, on_delete):
    global page_number_ref, table_ref, pagination_ref, goto

    page_number_ref = ft.Ref[int]() # Armazena o número da página atual
    page_number_ref.current = 0

    table_ref = ft.Ref[ft.DataTable]()
    pagination_ref = ft.Ref[ft.Row]()

    def goto(page_number, scroll=True):
        data = get_data(**{key: ref.current.value for key, ref in get_data_parameters.items()})

        page_number_ref.current = max(0, min(page_number, get_number_of_pages(data) - 1)) # Atualiza o número da página atual, garantindo que ele esteja entre 0 e o número máximo de páginas

        table_ref.current.rows = render_data(data, page_number_ref.current, rows_per_page, on_delete)
        
        pagination_ref.current.controls = render_pages(data)
        pagination_ref.current.width = min(500, len(pagination_ref.current.controls) * pagination_ref.current.controls[0].width)

        if scroll:
            pagination_ref.current.scroll_to(key=str(page_number_ref.current))

        page.update()

    return goto, ft.Column([
        ft.DataTable(
            ref=table_ref,
            columns=[ft.DataColumn(ft.Text(title), **styles["table-columns"]) for title in columns],
            **styles["table"]
        ),

        ft.Container(
            ft.Row(
                [
                    ft.IconButton(ft.Icons.CHEVRON_LEFT, tooltip="Anterior", on_click=lambda e: goto(page_number_ref.current - 1)),
                    ft.Row(ref=pagination_ref, **styles["pagination-pages"]),
                    ft.IconButton(ft.Icons.CHEVRON_RIGHT, tooltip="Próxima", on_click=lambda e: goto(page_number_ref.current + 1))
                ],
                **styles["pagination-row"]
            ),
            **styles["pagination-container"]
        )
    ])

styles = {
    "table": {
        "width": float("inf"),
        "border": ft.border.all(1, "#E0E3E8"),
        
        # Estilos Header
        "heading_row_height": 50,
        "heading_row_color": "#ECF0F3",
        "heading_text_style": ft.TextStyle(
            color="#556064",
            size=12,
            weight=ft.FontWeight.BOLD
        ),

        # Estilos Body
        "horizontal_lines": ft.BorderSide(
            color="#E0E3E8",
            width=1
        ),

        "data_row_min_height": 45,
        "data_row_max_height": 45,
        "data_text_style": ft.TextStyle(
            color="#959896",
            weight=ft.FontWeight.BOLD
        )
    },
    "table-columns": {
        "heading_row_alignment": ft.MainAxisAlignment.CENTER
    },
    
    "pagination-container": {
        "border": ft.border.all(1, "#E0E3E8"),
    },
    "pagination-row": {
        "alignment": ft.MainAxisAlignment.CENTER
    },
    "pagination-pages": {
        "spacing": 0,
        "alignment": ft.MainAxisAlignment.CENTER,
        "scroll": ft.ScrollMode.AUTO
    },

    "pagination-button": {
        "height": 40,
        "width": 40,
        "alignment": ft.alignment.center,
        "ink": True
    },
    "pagination-text": {
        "color": "#003565",
        "weight": ft.FontWeight.BOLD
    }
}