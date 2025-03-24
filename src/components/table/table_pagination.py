import typing as tp
import flet as ft

# Utils
from utils.pagination_util import get_total_pages

rows_per_page = 8


def pagination_buttons(total_pages: int, current_page: int, goto_page: tp.Callable) -> list[ft.Container]:
    """Cria os botões de paginação.

    Args:
        total_pages (int): Número total de páginas
        current_page (int): Página atual

    Returns:
        list[ft.Container]: Botões de paginação
    """
    # Componentes
    return [
        ft.Container(
            ft.Text(i+1, **styles["pagination-text"]),
            key=i,
            bgcolor="#E1E1E1" if i == current_page else "transparent",
            on_click=lambda e: goto_page(e.control.key),
            **styles["pagination-button"]
        )
        for i in range(total_pages)
    ]


def pagination(get_data: tp.Callable, get_data_parameters: dict[str, tp.Any], update_rows: tp.Callable, page: ft.Page) -> tuple[tp.Callable, ft.Container]:
    """Componente de paginação.

    Args:
        get_data (tp.Callable): Função para obter os dados
        get_data_parameters (dict[str, tp.Any]): Parâmetros para obter os dados
        update_rows (tp.Callable): Função para atualizar as linhas da tabela
        page (ft.Page): Página atual

    Returns:
        goto (tp.Callable): Função para ir para uma página específica
        ft.Container: Componente de paginação
    """
    # Referências
    pagination_ref = ft.Ref[ft.Row]()
    current_page_ref = ft.Ref[int]()
    current_page_ref.current = 0

    # Funções
    def update_pagination(total_pages: int) -> None:
        """Atualiza os botões de paginação.

        Args:
            total_pages (int): Número total de páginas
        """
        pagination_ref.current.controls = pagination_buttons(total_pages, current_page_ref.current, goto) # Gera os botões de paginação
        pagination_ref.current.width = min(500, len(pagination_ref.current.controls) * pagination_ref.current.controls[0].width) # Atualiza a largura do container de paginação, limitando a 500

        try:
            pagination_ref.current.scroll_to(key=str(current_page_ref.current)) # Rola a páginação para o botão da página atual
        except AssertionError:
            pass

    def goto(page_number: int = 0) -> None:
        """Vai para uma página específica, atualiza os dados e a paginação.

        Args:
            page_number (int): Número da página
        """
        data = get_data(**{key: ref.current.value for key, ref in get_data_parameters.items()}) # Obtém os dados

        total_pages = get_total_pages(data, rows_per_page)
        current_page_ref.current = max(0, min(page_number, total_pages - 1)) # Atualiza a página atual, garantindo que ela esteja entre 0 e o número máximo de páginas

        update_rows(data, current_page_ref.current, rows_per_page) # Atualiza as linhas da tabela

        update_pagination(total_pages)
        page.update()

    # Eventos
    def previous_page(e: ft.TapEvent):
        goto(current_page_ref.current - 1)

    def next_page(e: ft.TapEvent):
        goto(current_page_ref.current + 1)

    # Componente
    return goto, ft.Container(
        ft.Row(
            [
                ft.IconButton(
                    ft.Icons.CHEVRON_LEFT,
                    tooltip="Anterior",
                    on_click=previous_page
                ),

                ft.Row(ref=pagination_ref, **styles["pagination-pages"]),

                ft.IconButton(
                    ft.Icons.CHEVRON_RIGHT,
                    tooltip="Próxima",
                    on_click=next_page
                )
            ],
            **styles["pagination-row"]
        ),
        **styles["pagination-container"]
    )


# Estilos
styles = {
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