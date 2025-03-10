import sys
sys.path.insert(0, r"C:\Users\taygo\Downloads\PASTA DE TESTE\utils")

from data import validar_datas, validar_intervalo, validar_reservas

caminho = "data/reservas.csv" # Caminho do arquivo onde os dados das reservas serão armazenados 
campos = ["codigo-espaco", "dono-reserva", "datah-inicio","datah-fim"] # Campos que serão armazenados no arquivo

def criar_reserva() -> None: 
    """Cria o arquivo onde terão as informações das reservas 
    """

    # Escreve o cabeçalho no arquivo, mesmo que ele já exista
    with open(caminho, "w", encoding="utf-8") as arquivo: 
        arquivo.write(",".join(campos) + "\n")


def get_all() -> list:
    """Retorna uma lista com as reservas cadastradas
    """

    # Abre e lê todas as linhas, exceto a primeira que é o cabecalho, e cria um dicionário para cada linha
    with open(caminho, "r", encoding="utf-8") as arquivo: 
        return [dict(zip(campos,linha.strip().split(","))) for linha in arquivo.readlines()[1:]]

def get_by_codigo_espaco(codigo_espaco: str) -> list:
    """Retorna uma lista com as reservas de um determinado espaço

    Args:
        codigo_espaco (str): Código do espaço
    """

    # Retorna todas as reservas que possuem o código do espaço igual ao código passado
    return [reserva for reserva in get_all() if reserva["codigo-espaco"] == codigo_espaco]


def inserir(codigo_espaco: str, dono_reserva: str, datah_inicio: str, datah_fim: str):
    """Insere uma nova reserva no arquivo.

    Args:
        codigo_espaco (str): codigo do espaço.
        dono_reserva (str): dono da reserva.
        datah_inicio (str): data e hora de início, no formato "YYYY-MM-DD hh:mm".
        datah_fim (str): data e hora do fim, no formato "YYYY-MM-DD hh:mm".

    Raises:
        ValueError: Se a data início for antes que a data atual.
        ValueError: Se o tempo da reserva for menor que 30 minutos.
        ValueError: Se o intervalo da reserva coincidir com o intervalo de outra reserva.
    """

    if not validar_datas(datah_inicio):
        raise ValueError("Data de início não pode ser antes da data atual.")
    
    if not validar_intervalo(datah_inicio, datah_fim):
        raise ValueError("Intervalo da reserva deve ser de no mínimo 30 minutos.")
    
    if any([not validar_reservas(datah_inicio, datah_fim, reserva["datah-inicio"], reserva["datah-fim"]) for reserva in get_by_codigo_espaco(codigo_espaco)]):
        raise ValueError("Intervalo da reserva coincide com o intervalo de outra reserva.")

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo_espaco},{dono_reserva},{datah_inicio},{datah_fim}\n")


# inserir("1", "João", "2021-10-10 10:00", "2021-10-10 11:00")
# inserir("1", "João", "2025-10-10 12:00", "2025-10-10 12:15")
# inserir("1", "João", "2025-10-10 12:00", "2025-10-10 12:45")
# inserir("1", "João", "2025-10-10 12:00", "2025-10-10 12:45")
# inserir("6", "João", "2025-10-10 12:00", "2025-10-10 12:45")