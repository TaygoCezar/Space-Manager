from datetime import datetime

def format_date(date_str: str) -> str:
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    
    months = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    month = months[date.month - 1]
    return date.strftime(f"%d de {month} de %Y, %H:%M")

def categorize_interval(start_str: str, end_str: str) -> str:
    start = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
    end = datetime.strptime(end_str, "%Y-%m-%d %H:%M")
    
    now = datetime.now()
    
    if end < now:
        return "gone"
    
    elif start <= now:
        return "on going"
    
    else:
        return "scheduled"