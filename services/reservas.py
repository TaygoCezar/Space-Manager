caminho = "data/reservas.csv" 
campos = ["espaco", "dono-reserva", "datah-inicio","datah-fim"]

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


print(get_all())


def inserir():
    pass