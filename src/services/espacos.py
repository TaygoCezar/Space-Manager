import sys, pathlib
sys.path.insert(0, pathlib.Path(__file__).parent.parent)

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