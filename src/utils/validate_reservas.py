from datetime import timedelta, datetime as dt

from services.reservas import get_all

def validate_dono(dono):
    if dono == "":
        return "O campo 'Dono' é obrigatório"


def validate_espaco(espaco):
    if espaco == "":
        return "O campo 'Espaço' é obrigatório"


def validate_data(data):
    if data == "":
        return "O campo é obrigatório"

    try:
        dt.strptime(data, "%d/%m/%Y")
    except ValueError:
        return "Data inválida"


def validate_horario(horario):
    if horario == "":
        return "O campo é obrigatório"

    try:
        dt.strptime(horario, "%H:%M")
    except ValueError:
        return "Horário inválido"


def validate_data_hora(data, horario):
    data = dt.strptime(data, "%d/%m/%Y")
    horario = dt.strptime(horario, "%H:%M")

    now = dt.strptime(dt.now().strftime("%d/%m/%Y %H:%M"), "%d/%m/%Y %H:%M")

    data_hora = dt.combine(data, horario.time())
    if data_hora < now:
        return "A reserva não pode ser feita para um horário passado"
    
def validate_intervalo(codigo_espaco, data_inicio, horario_inicio, data_termino, horario_termino, exlude_id=None):
    data_hora_inicio = dt.combine(dt.strptime(data_inicio, "%d/%m/%Y"), dt.strptime(horario_inicio, "%H:%M").time())
    data_hora_termino = dt.combine(dt.strptime(data_termino, "%d/%m/%Y"), dt.strptime(horario_termino, "%H:%M").time())

    if data_hora_inicio > data_hora_termino:
        return "A data de inicio deve ser anterior à data de término"
    
    if data_hora_termino - data_hora_inicio < timedelta(minutes=30):
        return "A reserva deve ter duração mínima de 30 minutos"
    
    for reserva in get_all():
        if reserva["id"] == exlude_id:
            continue

        if reserva["codigo-espaco"] == codigo_espaco:
            reserva_data_hora_inicio = dt.strptime(reserva["inicio"], "%Y-%m-%d %H:%M")
            reserva_data_hora_termino = dt.strptime(reserva["fim"], "%Y-%m-%d %H:%M")
    
            if reserva_data_hora_inicio < data_hora_termino and data_hora_inicio < reserva_data_hora_termino:
                return "O espaço já está reservado para esse intervalo de tempo"