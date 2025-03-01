caminho = "data/espacos.csv" # Caminho do arquivo onde os dados dos espaços serão armazenados
campos = ["codigo", "nome"] # Campos que serão armazenados no arquivo

def criar_arquivo() -> None:
    """Cria o arquivo onde serão armazenados os dados dos espaços.
    """

    # Escreve o cabeçalho no arquivo, mesmo que ele já exista
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(campos) + "\n")


def get_all() -> list:
    """Retorna uma lista com todos os espaços cadastrados.

    Returns:
        list: Lista com todos os espaços cadastrados.
    """

    # Abre o arquivo e lê todas as linhas, exceto a primeira que é o cabeçalho, e cria um dicionário para cada linha
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return [dict(zip(campos, linha.strip().split(","))) for linha in arquivo.readlines()[1:]]


def inserir(codigo: str, nome: str) -> None:
    """Insere um novo espaço no arquivo.

    Args:
        codigo (str): codigo do espaço.
        nome (str): nome do espaço.

    Raises:
        ValueError: Se o código do espaço já existir.
    """

    # Verifica se o código já existe, caso exista, levanta um ValueError
    if any([codigo == espaco["codigo"] for espaco in get_all()]):
      raise ValueError(f"O código {codigo} já existe.")

    # Insere o novo espaço no arquivo
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo},{nome}\n")