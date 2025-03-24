from datetime import datetime as dt, timedelta

# Serviços
from services.reservas_service import Reserva, get_all_reservas

# Utils
from utils.date_util import format_date, categorize_interval, date_dist
from utils.search_util import prefix_check


def get_reservas_by_key_and_mode(key: str, mode: str) -> list[Reserva]:
    """Retorna todas as reservas que possuem algum campo com o prefixo da chave passada, ignorando diferenças entre maiúsculas e minúsculas, e letras acentuadas. Além disso, filtra as reservas com base no modo de visualização selecionado.

    Args:
        key (str): Chave para a busca.
        mode (str): Modo de visualização.

    Returns:
        list[Reserva]: Lista de reservas que possuem algum campo com o prefixo da chave passada e que se encaixam no modo de visualização selecionado.
    """
    reservas = get_all_reservas()

    reservas.sort(key=lambda reserva: date_dist(reserva["inicio"])) # Ordena as reservas por data de início. Verifique a função date_dist no arquivo utils/date_utils.py

    def map_reserva(reserva: Reserva) -> Reserva:
        reserva["status"] = categorize_interval(reserva["inicio"], reserva["fim"])

        reserva["formatted-inicio"] = format_date(reserva["inicio"])
        reserva["formatted-fim"] = format_date(reserva["fim"])

        return reserva
    reservas = map(map_reserva, reservas)

    def filter_reserva(reserva: Reserva) -> bool:
        return any([prefix_check(value, key) for value in reserva.values()]) and (mode == "all" or reserva["status"] != "Finalizada") # Verifica se algum campo da reserva possui o prefixo da chave passada. Verifique a função prefix_check no arquivo utils/search_utils.py
    reservas = filter(filter_reserva, reservas)

    return list(reservas)


def validate_dono(dono: str) -> str|None:
    """Verifica se o dono é válido.

    Args:
        dono (str): Dono.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """
    if dono == "":
        return "O campo 'Dono' é obrigatório"

    return None


def validate_espaco(codigo_espaco: str) -> str|None:
    """Verifica se o código do espaço é válido.

    Args:
        codigo_espaco (str): Código do espaço.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """
    if codigo_espaco == "":
        return "O campo 'Espaço' é obrigatório"

    return None


def validate_data(data: str) -> str|None:
    """Verifica se a data é válida.

    Args:
        data (str): Data.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """
    if data == "":
        return "O campo é obrigatório"

    try:
        dt.strptime(data, "%d/%m/%Y")
    except ValueError:
        return "Data inválida"

    return None


def validate_horario(horario: str) -> str|None:
    """Verifica se o horário é válido.

    Args:
        horario (str): Horário.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """
    if horario == "":
        return "O campo é obrigatório"

    try:
        dt.strptime(horario, "%H:%M")
    except ValueError:
        return "Horário inválido"

    return None


def validate_data_hora(data: str, horario: str) -> str|None:
    """Verifica se a data e o horário são válidos.

    Args:
        data (str): Data.
        horario (str): Horário.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """
    data = dt.strptime(data, "%d/%m/%Y")
    horario = dt.strptime(horario, "%H:%M")

    now = dt.strptime(dt.now().strftime("%d/%m/%Y %H:%M"), "%d/%m/%Y %H:%M")

    data_hora = dt.combine(data, horario.time())
    if data_hora < now:
        return "A reserva não pode ser feita para um horário passado"

    return None


def validate_intervalo(codigo_nome_espaco: str, data_inicio: str, horario_inicio: str, data_termino: str, horario_termino: str, exclude_codigo: str=None) -> str|None:
    """Verifica se o intervalo de tempo é válido.

    Args:
        codigo_espaco (str): Código do espaço.
        data_inicio (str): Data de início.
        horario_inicio (str): Horário de início.
        data_termino (str): Data de término.
        horario_termino (str): Horário de término.
        exclude_codigo (str): Código da reserva a ser excluída da verificação.

    Returns:
        str|None: Mensagem de erro, se houver. None caso contrário.
    """
    codigo_espaco = codigo_nome_espaco.split(",")[0]
    data_hora_inicio = dt.combine(dt.strptime(data_inicio, "%d/%m/%Y"), dt.strptime(horario_inicio, "%H:%M").time())
    data_hora_termino = dt.combine(dt.strptime(data_termino, "%d/%m/%Y"), dt.strptime(horario_termino, "%H:%M").time())

    if data_hora_inicio > data_hora_termino:
        return "A data de inicio deve ser anterior à data de término"

    if data_hora_termino - data_hora_inicio < timedelta(minutes=30):
        return "A reserva deve ter duração mínima de 30 minutos"

    for reserva in get_all_reservas():
        if reserva["codigo-espaco"] == codigo_espaco and reserva["codigo"] != exclude_codigo:
            reserva_data_hora_inicio = dt.strptime(reserva["inicio"], "%Y-%m-%d %H:%M")
            reserva_data_hora_termino = dt.strptime(reserva["fim"], "%Y-%m-%d %H:%M")

            if reserva_data_hora_inicio < data_hora_termino and data_hora_inicio < reserva_data_hora_termino:
                return "O intervalo de tempo escolhido está ocupado"

    return None