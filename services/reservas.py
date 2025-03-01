caminho = "data/reservas.csv" 
campos = ["codigo_espaco", "dono-reserva", "datah-inicio","datah-fim"]

def criar_reserva() -> None: 
    """Cria o arquivo onde terão as informações das reservas 
    """
    with open(caminho, "w", encoding="utf-8") as arquivo: 
        arquivo.write(",".join(campos) + "\n")
    
def get_all() -> list:
    """Retorna uma lista com as reservas cadastradas
    """ 
    with open(caminho, "r", encoding="utf-8") as arquivo: 
        return [dict(zip(campos,linha.strip().split(","))) for linha in arquivo.readlines()[1:]]

def inserir_reservas(codigo_espaco: str, dono_reserva: str, datah_inicio: str, datah_fim: str) -> None:
    """Cria uma nova reserva 

    Args:  
        codigo_espaco (str): espaço da reserva
        dono_reserva (str): nome do dono da reserva
        datah_inicio (str): data e hora de inicio no formato YYYY-MM-DD hh:mm
        datah_fim (str): data e hora de fim no formato YYYY-MM-DD hh:mm
    
    Raises: 
        ValueError: Se o fim for menos de 30 minutos depois do inicio. 
    """

    

    with open(caminho, "a", encoding="utf-8") as arquivo: 
        arquivo.write(f"{codigo_espaco},{dono_reserva},{datah_inicio},{datah_fim}\n")

inserir_reservas("mesa 09", "murilo henrique", "2025-06-29 14:30", "2025-06-29 16:30")

    # with open(caminho, "a", encoding="utf-8") as arquivo: 
    #     arquivo.write(",".join([nova_reserva[campo] for campo in campos])) 


