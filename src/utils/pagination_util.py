import math


def get_total_pages(data: list[dict], rows_per_page) -> int:
    """Calcula o número de páginas necessárias para exibir todos os dados.

    Args:
        data (list[dict]): Dados

    Returns:
        int: Número de páginas
    """
    number_of_rows = len(data)
    return max(1, math.ceil(number_of_rows / rows_per_page))