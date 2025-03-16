from datetime import datetime as dt

def format_date(date_str: str) -> str:
    date = dt.strptime(date_str, "%Y-%m-%d %H:%M")
    
    months = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    month = months[date.month - 1]
    return date.strftime(f"%d de {month} de %Y, %H:%M")

def categorize_interval(start_str: str, end_str: str) -> str:
    start = dt.strptime(start_str, "%Y-%m-%d %H:%M")
    end = dt.strptime(end_str, "%Y-%m-%d %H:%M")
    
    now = dt.now()
    
    if end < now:
        return "Finalizada"
    
    elif start <= now:
        return "Em andamento"
    
    else:
        return "Agendada"