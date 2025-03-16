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
    
def get_by_id(id: str) -> dict:
    """Retorna a reserva com o id especificado
    """
    
    reservas = get_all()
    
    for reserva in reservas:
        if reserva["id"] == id:
            return reserva
    
    return None

def save_reservas(reservas: list[dict]) -> None:
    """Salva as reservas no arquivo
    """
    
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(campos)+"\n") # -> "id,codigo-espaco,nome-espaco,dono,inicio,fim\n"

        for reserva in reservas:
            arquivo.write(",".join(reserva.values())+"\n")


def add_reserva(codigo_espaco, nome_espaco, dono, inicio, fim) -> None:
    """Adiciona uma reserva ao arquivo
    """

    reservas = get_all()
    max_id = int(reservas[-1]["id"]) if len(reservas) > 0 else 0
    
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{max_id+1},{codigo_espaco},{nome_espaco},{dono},{inicio},{fim}\n")


def update_reserva(id: str, codigo_espaco, nome_espaco, dono, inicio, fim) -> None:
    """Atualiza uma reserva no arquivo
    """
    
    reservas = get_all()

    for reserva in reservas:
        if reserva["id"] == id:
            reserva["codigo-espaco"] = codigo_espaco
            reserva["nome-espaco"] = nome_espaco
            reserva["dono"] = dono
            reserva["inicio"] = inicio
            reserva["fim"] = fim

            save_reservas(reservas)
            return


def delete_reserva(id: str):
    reservas = get_all()

    for reserva in reservas.copy(): 
        if reserva["id"] == id:
            reservas.remove(reserva)
    
    save_reservas(reservas) 