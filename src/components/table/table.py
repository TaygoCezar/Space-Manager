import typing as tp
import flet as ft

# Componentes Customizados
from components.table.table_pagination import pagination


def table(get_data: tp.Callable, get_data_parameters: dict[str, tp.Any], columns: list[str], row: tp.Callable, page: ft.Page) -> tuple[tp.Callable, ft.Column]:
    """Componente de tabela.

    Args:
        get_data (tp.Callable): Função para obter oss dados
        get_data_parameters (dict[str, tp.Any]): Parâmetros para obter os dados
        columns (list[str]): Colunas
        row (tp.Callable): Função para renderizar uma linha
        page (ft.Page): Página atual
    
    Returns:
        goto (tp.Callable): Função para ir para uma página específica
        ft.Column: Componente de tabela
    """
    table_ref = ft.Ref[ft.DataTable]()

    # Funcões
    def update_rows(data: list[dict], current_page, rows_per_page) -> None:
        """Atualiza as linhas da tabela.

        Args:
            data (list[dict]): Dados
            current_page (int): Página atual
            rows_per_page (int): Número de linhas por página
        """
        start = current_page * rows_per_page # Indice inicial dos dados
        end = start + rows_per_page # Indice final dos dados

        table_ref.current.rows = list(map(lambda data: row(data, goto), data[start:end])) # Atualiza as linhas da tabela

    # Componentes
    goto, pagination_component = pagination(get_data, get_data_parameters, update_rows, page) 

    return goto, ft.Column([
        ft.DataTable(
            ref=table_ref,
            columns=[ft.DataColumn(ft.Text(title), **styles["table-columns"]) for title in columns],
            **styles["table"]
        ),

        pagination_component
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
}