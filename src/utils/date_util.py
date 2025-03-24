from datetime import datetime as dt, timedelta


def format_date(date_str: str) -> str:
    """Formata a data no formato "dia de mês de ano, hora:minuto".

    Args:
        date_str (str): Data no formato "ano-mês-dia hora:minuto".

    Returns:
        str: Data formatada.
    """
    date = dt.strptime(date_str, "%Y-%m-%d %H:%M")
    
    months = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    month = months[date.month - 1]

    return date.strftime(f"%d de {month} de %Y, %H:%M")


def categorize_interval(start_str: str, end_str: str) -> str:
    """Categoria o intervalo de tempo em que a reserva se encontra em "Finalizada", "Em andamento" ou "Agendada".

    Args:
        start_str (str): Data de início no formato "ano-mês-dia hora:minuto".
        end_str (str): Data de fim no formato "ano-mês-dia hora:minuto".

    Returns:
        str: Categoria da reserva.
    """
    start = dt.strptime(start_str, "%Y-%m-%d %H:%M")
    end = dt.strptime(end_str, "%Y-%m-%d %H:%M")
    
    now = dt.now()
    
    if end < now:
        return "Finalizada"
    
    elif start <= now:
        return "Em andamento"
    
    else:
        return "Agendada"
    

def date_dist(start_str: str) -> timedelta:
    """Calcula a diferença entre a data de início e a data atual.

    Args:
        start_str (str): Data de início no formato "ano-mês-dia hora:minuto".

    Returns:
        str: Diferença entre a data de início e a data atual.
    """
    start = dt.strptime(start_str, "%Y-%m-%d %H:%M")
    now = dt.now()
    
    return abs(now - start)


def convert_str_date_to_format(date_str: str) -> str:
    """Converte a data no formato "dia/mês/ano" para "ano-mês-dia"."

    Args:
        date_str (str): Data no formato "dia/mês/ano".

    Returns:
        str: Data no formato "ano-mês-dia".
    """
    date = dt.strptime(date_str, "%d/%m/%Y")
    return date.strftime("%Y-%m-%d")


def convert_format_date_to_str(date_str: str) -> tuple[str, str]:
    """Converte a data no formato "ano-mês-dia hora:minuto" para "dia/mês/ano" e "hora:minuto".

    Args:
        date_str (str): Data no formato "ano-mês-dia".

    Returns:
        str: Data no formato "dia/mês/ano".
        str: Hora no formato "hora:minuto".
    """
    date = dt.strptime(date_str, "%Y-%m-%d %H:%M")
    return date.strftime("%d/%m/%Y"), date.strftime("%H:%M")