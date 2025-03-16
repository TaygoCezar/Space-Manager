import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

from services.reservas import get_all as get_all_reservas, save_reservas

caminho = "data/espacos.csv" # Caminho do arquivo onde os dados dos espaços serão armazenados
campos = ["codigo", "nome"] # Campos que serão armazenados no arquivo

def criar_espaco() -> None:
    """Cria o arquivo onde terão as informações dos espaços
    """

    # Escreve o cabeçalho no arquivo, mesmo que ele já exista
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(campos) + "\n")

def get_all() -> list:
    """Retorna uma lista com os espaços cadastrados
    """

    # Abre e lê todas as linhas, exceto a primeira que é o cabecalho, e cria um dicionário para cada linha
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return [dict(zip(campos,linha.strip().split(","))) for linha in arquivo.readlines()[1:]]
    except:
        criar_espaco()
        return []
    
def get_by_codigo(codigo: str) -> dict:
    espacos = get_all()

    for espaco in espacos:
        if espaco["codigo"] == codigo:
            return espaco
    

def save_espacos(espacos: list[dict]) -> None:
    """Salva os espaços no arquivo
    """

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(campos)+"\n")

        for espaco in espacos:
            arquivo.write(",".join(espaco.values())+"\n")

def add_espaco(codigo: str, nome: str) -> None:
    """Adiciona um espaço ao arquivo
    """

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo},{nome}\n")

def update_espaco(codigo: str, novo_codigo: str, nome: str) -> None:
    """Atualiza um espaço no arquivo
    """

    espacos = get_all()

    for espaco in espacos:
        if espaco["codigo"] == codigo:
            espaco["codigo"] = novo_codigo
            espaco["nome"] = nome
            break

    save_espacos(espacos)

    reservas = get_all_reservas()
    for reserva in reservas:
        if reserva["codigo-espaco"] == codigo:
            reserva["codigo-espaco"] = novo_codigo
            reserva["nome-espaco"] = nome

    save_reservas(reservas)

def delete_espaco(codigo: str) -> None:
    """Deleta um espaço do arquivo
    """

    espacos = get_all()

    for espaco in espacos:
        if espaco["codigo"] == codigo:
            espacos.remove(espaco)
            break

    save_espacos(espacos)

    reservas = get_all_reservas()
    reservas = [reserva for reserva in reservas if reserva["codigo-espaco"] != codigo]

    save_reservas(reservas)