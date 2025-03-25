from services.reservas_service import update_reservas_codigo_espaco, delete_reservas_by_codigo_espaco

caminho = "data/espacos.csv" # Caminho do arquivo onde os dados dos espaços serão armazenados
campos = ["codigo", "nome"] # Campos que serão armazenados no arquivo

# Interfaces
Espaco = dict["codigo": str, "nome": str] # Tipo de dado que representa um espaço


def create_espacos_file() -> None:
    """Cria o arquivo onde serão armazenadas as informações sobre os espaços
    """
    # Escreve o cabeçalho no arquivo, mesmo que ele já exista
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(campos)+"\n")


def ensure_espacos_file() -> None:
    """Verifica se o arquivo onde os espaços são armazenados existe, e se tem o cabeçalho, caso contrário, cria o arquivo
    """

    try: 
        with open(caminho, "r", encoding="utf-8") as arquivo: # Tenta abrir o arquivo para leitura
            if len(arquivo.readlines()) == 0:
                raise FileNotFoundError # Se o arquivo estiver vazio, lança um erro
            
    except FileNotFoundError: # Caso o arquivo não exista
        create_espacos_file() # Cria o arquivo


def save_espacos(espacos: list[Espaco]) -> None:
    """Recebe uma lista de espaços e salva no arquivo, sobrescrevendo o conteúdo anterior

    Args:
        espacos (list[espaco]): Lista de espaços
    """
    create_espacos_file() # Cria o arquivo, apagando o conteúdo existente

    with open(caminho, "a", encoding="utf-8") as arquivo: # Abre o arquivo para escrita
        for espaco in espacos:
            arquivo.write(",".join(espaco.values())+"\n") # Escreve cada espaço no arquivo, separando os valores por vírgula e adicionando uma quebra de linha no final


def add_espaco(codigo: str, nome: str) -> None:
    """Adiciona um espaço ao arquivo

    Args:
        codigo (str): Código do espaço
        nome (str): Nome do espaço
    """
    ensure_espacos_file() # Verifica se o arquivo existe

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo},{nome}\n") # Adiciona o novo espaço ao arquivo


def get_all_espacos() -> list[Espaco]:
    """Retorna todos os espaços armazenados no arquivo

    Returns:
        list[espaco]: Lista de espaços
    """
    ensure_espacos_file() # Verifica se o arquivo existe

    with open(caminho, "r", encoding="utf-8") as arquivo: # Lê o arquivo
        return [dict(zip(campos, linha.strip().split(","))) for linha in arquivo.readlines()[1:]] # Cria um dicionário para cada linha do arquivo, onde as chaves são os campos e os valores são os valores da linha
    

def get_espaco_by_codigo(codigo: str) -> Espaco|None:
    """Retorna um espaço a partir de seu código

    Args:
        codigo (str): Código do espaço

    Returns:
        Espaco|None: Espaço encontrado ou None caso não encontre
    """
    espacos = get_all_espacos() # Obtém todos os espaços

    for espaco in espacos: # Percorre todos os espaços e retorna o espaço caso o código seja igual ao código passado
        if espaco["codigo"] == codigo: 
            return espaco
    
    return None # Caso não encontre o espaço, retorna None


def update_espaco(codigo: str, new_codigo: str, nome: str) -> None:
    """Atualiza um espaço no arquivo, a partir de seu código

    Args:
        codigo (str): Código do espaço a ser atualizado
        novo_codigo (str): Novo código do espaço
        nome (str): Novo nome do espaço
    """
    espacos = get_all_espacos() # Obtém todos os espaços

    def update_espaco(espaco: Espaco) -> Espaco:
        """Atualiza um espaço, caso o código seja igual ao código passado, alterando o código e o nome. Também atualiza as reservas associadas ao espaço

        Args:
            espaco (Espaco): Espaço a ser atualizado

        Returns:
            Espaco: Espaço atualizado
        """
        if espaco["codigo"] == codigo:
            espaco["codigo"] = new_codigo
            espaco["nome"] = nome

        return espaco
    
    espacos = list(map(update_espaco, espacos)) # Atualiza o espaços
    save_espacos(espacos) # Salva os espaços no arquivo, sobrescrevendo o conteúdo anterior

    update_reservas_codigo_espaco(codigo, new_codigo, nome) # Atualiza as reservas associadas ao espaço


def delete_espaco(codigo: str) -> None:
    """Deleta um espaço do arquivo, removendo-o a partir de seu código. Também remove todas as reservas associadas ao espaço
    
    Args:
        codigo (str): Código do espaço a ser deletado
    """
    espacos = get_all_espacos() # Obtém todos os espaços

    def filter_espaco(espaco: Espaco) -> bool:
        """Filtra os espaços, removendo o espaço com o código passado

        Args:
            espaco (Espaco): Espaço a ser filtrado

        Returns:
            bool: True se o espaço não for o espaço a ser removido, False caso contrário
        """
        return espaco["codigo"] != codigo

    espacos = list(filter(filter_espaco, espacos)) # Filtra os espaços, removendo o espaço com o código passado
    save_espacos(espacos) # Salva os espaços no arquivo, sobrescrevendo o conteúdo anterior

    delete_reservas_by_codigo_espaco(codigo) # Deleta as reservas associadas ao espaço