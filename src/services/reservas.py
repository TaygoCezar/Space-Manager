import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

caminho = "data/reservas.csv" # Caminho do arquivo onde os dados das reservas serão armazenados 
campos = ["id", "codigo-espaco", "nome-espaco", "dono", "inicio", "fim"] # Campos que serão armazenados no arquivo

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
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo: 
            return [dict(zip(campos,linha.strip().split(","))) for linha in arquivo.readlines()[1:]]
    except:
        criar_reserva()
        return []

def save_reservas(reservas: list[dict]) -> None:
    """Salva as reservas no arquivo
    """
    
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(campos)+"\n") # -> "id,codigo-espaco,nome-espaco,dono,inicio,fim\n"

        for reserva in reservas:
            arquivo.write(",".join(reserva.values())+"\n")


def delete_reserva(id: str):
    reservas = get_all()

    for reserva in reservas.copy(): 
        if reserva["id"] == id:
            reservas.remove(reserva)
    
    save_reservas(reservas) 