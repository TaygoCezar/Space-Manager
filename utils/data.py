import datetime as dt

def validar_datas(datah_inicio_string: str) -> bool:
    """Verifica se a data inicio é depois da data atual.

    Args: 
        datah_inicio_string (str): data e hora de início, no formato "YYYY-MM-DD hh:mm".
    """

    datah_atual = dt.datetime.now() # Busca a data e hora atual 
    datah_inicio = dt.datetime.strptime(datah_inicio_string, "%Y-%m-%d %H:%M") # Converte a string para datetime
    
    return datah_inicio > datah_atual  # Verifica se a data de início é depois da data atual

def validar_intervalo(datah_inicio_string: str, datah_fim_string: str) -> bool:
    """Verifica se o intervalo mínimo da reserva é de 30 minutos.

    Args: 
        datah_inicio_string (str): data e hora de início, no formato "YYYY-MM-DD hh:mm".
        datah_fim_string (str): data e hora do fim, no formato "YYYY-MM-DD hh:mm".
     """
    
    # Converte datah_inicio e datah_fim para datetime
    datah_inicio = dt.datetime.strptime(datah_inicio_string, "%Y-%m-%d %H:%M")
    datah_fim = dt.datetime.strptime(datah_fim_string, "%Y-%m-%d %H:%M")

    intervalo = datah_fim - datah_inicio # Calcula o intervalo entre as datas
    intervalo_minutos = intervalo.total_seconds()/60 # Converte o intervalo para minutos
    
    return intervalo_minutos >= 30 # Verifica se o intervalo é maior ou igual a 30 minutos

def validar_reservas(reserva_1_inicio_string: str, reserva_1_fim_string: str, reserva_2_inicio_string: str, reserva_2_fim_string: str) -> bool:
    """Verifica se duas reservas não possuem conflito de horário.

    Args:
        reserva_1_inicio_string (str): data e hora de início da primeira reserva, no formato "YYYY-MM-DD hh:mm".
        reserva_1_fim_string (str): data e hora do fim da primeira reserva, no formato "YYYY-MM-DD hh:mm".

        reserva_2_inicio_string (str): data e hora de início da segunda reserva, no formato "YYYY-MM-DD hh:mm".
        reserva_2_fim_string (str): data e hora do fim da segunda reserva, no formato "YYYY-MM-DD hh:mm".
    """

    # Converte as datas para datetime
    reserva_1_inicio = dt.datetime.strptime(reserva_1_inicio_string, "%Y-%m-%d %H:%M")
    reserva_1_fim = dt.datetime.strptime(reserva_1_fim_string, "%Y-%m-%d %H:%M")

    reserva_2_inicio = dt.datetime.strptime(reserva_2_inicio_string, "%Y-%m-%d %H:%M")
    reserva_2_fim = dt.datetime.strptime(reserva_2_fim_string, "%Y-%m-%d %H:%M")

    # Verifica se a reserva 1 termina antes da reserva 2 começar ou se a reserva 2 termina antes da reserva 1 começar
    return reserva_1_fim <= reserva_2_inicio or reserva_2_fim <= reserva_1_inicio