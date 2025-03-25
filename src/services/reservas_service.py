caminho = "data/reservas.csv" # Caminho do arquivo onde os dados das reservas serão armazenados 
campos = ["codigo", "codigo-espaco", "nome-espaco", "dono", "inicio", "fim"] # Campos que serão armazenados no arquivo

# Interfaces
Reserva = dict["codigo": str, "codigo-espaco": str, "nome-espaco": str, "dono": str, "inicio": str, "fim": str] # Tipo de dado que representa uma reserva


def create_reservas_file() -> None: 
    """Cria o arquivo onde serão armazenadas as informações sobre as reservas
    """

    # Escreve o cabeçalho no arquivo, mesmo que ele já exista
    with open(caminho, "w", encoding="utf-8") as arquivo: 
        arquivo.write(",".join(campos) + "\n")


def ensure_reservas_file() -> None:
    """Verifica se o arquivo onde as reservas são armazenadas existe, e se tem o cabeçalho, caso contrário, cria o arquivo
    """

    try: 
        with open(caminho, "r", encoding="utf-8") as arquivo: # Tenta abrir o arquivo para leitura
            if len(arquivo.readlines()) == 0:
                raise FileNotFoundError # Se o arquivo estiver vazio, lança um erro
            
    except FileNotFoundError: # Caso o arquivo não exista
        create_reservas_file() # Cria o arquivo


def save_reservas(reservas: list[Reserva]) -> None:
    """Recebe uma lista de reservas e salva no arquivo, sobrescrevendo o conteúdo anterior

    Args:
        reservas (list[Reserva]): Lista de reservas
    """
    create_reservas_file() # Cria o arquivo, apagando o conteúdo existente

    with open(caminho, "w", encoding="utf-8") as arquivo: # Abre o arquivo para escrita
        for reserva in reservas:
            arquivo.write(",".join(reserva.values())+"\n") # Escreve cada reserva no arquivo, separando os valores por vírgula e adicionando uma quebra de linha no final


def add_reserva(codigo_espaco: str, nome_espaco: str, dono: str, inicio: str, fim: str) -> None:
    """Adiciona uma reserva ao arquivo

    Args:
        codigo_espaco (str): Código do espaço
        nome_espaco (str): Nome do espaço
        dono (str): Nome do dono da reserva
        inicio (str): Data de início da reserva
        fim (str): Data de fim da reserva
    """
    ensure_reservas_file() # Verifica se o arquivo existe

    reservas = get_all_reservas()
    max_codigo = int(reservas[-1]["codigo"]) if len(reservas) > 0 else 0 # Pega o maior codigo das reservas
    
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{max_codigo+1},{codigo_espaco},{nome_espaco},{dono},{inicio},{fim}\n") # Adiciona a nova reserva ao arquivo


def get_all_reservas() -> list[Reserva]:
    """Retorna todas as reservas armazenadas no arquivo

    Returns:
        list[Reserva]: Lista de reservas
    """
    ensure_reservas_file() # Verifica se o arquivo existe

    with open(caminho, "r", encoding="utf-8") as arquivo: # Lê o arquivo
        return [dict(zip(campos, linha.strip().split(","))) for linha in arquivo.readlines()[1:]] # Cria um dicionário para cada linha do arquivo, onde as chaves são os campos e os valores são os valores da linha
    

def get_reserva_by_codigo(codigo: str) -> Reserva|None:
    """Retorna uma reserva a partir de seu código

    Args:
        codigo (str): Código da reserva
    
    Returns:
        Reserva|None: Reserva encontrada ou None caso não encontre
    """
    reservas = get_all_reservas() # Obtém todas as reservas

    for reserva in reservas: # Percorre todas as reservas e retorna a reserva caso o código seja igual ao código
        if reserva["codigo"] == codigo:
            return reserva

    return None # Caso não encontre a reserva, retorna None


def update_reserva(codigo: str, codigo_espaco: str, nome_espaco: str, dono: str, inicio: str, fim: str) -> None:
    """Atualiza uma reserva no arquivo, a partir de seu código

    Args:
        codigo (str): Código da reserva a ser atualizada
        codigo_espaco (str): Código do espaço
        nome_espaco (str): Nome do espaço
        dono (str): Nome do dono da reserva
        inicio (str): Data de início da reserva
        fim (str): Data de fim da reserva
    """
    reservas = get_all_reservas() # Obtém todas as reservas

    def update_reserva(reserva: Reserva) -> Reserva:
        """Atualiza uma reserva, caso o código seja igual ao código passado, alterando o código do espaço, o nome do espaço, o dono, a data de início e a data de fim

        Args:
            reserva (Reserva): Reserva a ser atualizada
        
        Returns:
            Reserva: Reserva atualizada
        """
        if reserva["codigo"] == codigo:
            reserva["codigo-espaco"] = codigo_espaco
            reserva["nome-espaco"] = nome_espaco
            reserva["dono"] = dono
            reserva["inicio"] = inicio
            reserva["fim"] = fim

        return reserva

    reservas = list(map(update_reserva, reservas)) # Atualiza a reserva
    save_reservas(reservas) # Salva as reservas no arquivo, sobrescrevendo o conteúdo anterior


def update_reservas_codigo_espaco(codigo_espaco: str, new_codigo_espaco: str, nome_espaco: str) -> None:
    """Atualiza todas as reservas de um espaço no arquivo, a partir do codigo do espaço
    
    Args:
        codigo_espaco (str): Código dos espaco cuja reservas serão atualizadas
        new_codigo_espaco (str): Novo código do espaço
        nome_espaco (str): Novo nome do espaço
    """
    reservas = get_all_reservas() # Obtém todas as reservas

    def update_reserva(reserva: Reserva) -> Reserva:
        """Atualiza uma reserva, caso o código do espaço seja igual ao código passado, alterando o código do espaço e o nome do espaço
        
        Args:
            reserva (Reserva): Reserva a ser atualizada

        Returns:
            Reserva: Reserva atualizada
        """
        if reserva["codigo-espaco"] == codigo_espaco:
            reserva["codigo-espaco"] = new_codigo_espaco
            reserva["nome-espaco"] = nome_espaco

        return reserva

    reservas = list(map(update_reserva, reservas)) # Atualiza as reservas
    save_reservas(reservas) # Salva as reservas no arquivo, sobrescrevendo o conteúdo anteriorq


def delete_reserva(codigo: str) -> None:
    """Deleta uma reserva do arquivo, removendo-a a partir de seu código
    
    Args:
        codigo (str): Código da reserva a ser deletada
    """
    reservas = get_all_reservas() # Obtém todas as reservas

    def filter_reserva(reserva: Reserva) -> bool:
        """Filtra as reservas, removendo a reserva com o código passado

        Args:
            reserva (Reserva): Reserva a ser filtrada

        Returns:
            bool: True se a reserva não for a reserva com o código passado, False caso contrário
        """
        return reserva["codigo"] != codigo

    reservas = list(filter(filter_reserva, reservas)) # Filtra as reservas, removendo a reserva com o código passado
    save_reservas(reservas) # Salva as reservas no arquivo, sobrescrevendo o conteúdo anterior


def delete_reservas_by_codigo_espaco(codigo_espaco: str) -> None:
    """Deleta todas as reservas de um espaço no arquivo, a partir do codigo do espaço
    
    Args:
        codigo_espaco (str): Código dos espaco cujas reservas serão deletadas
    """
    reservas = get_all_reservas() # Obtém todas as reservas

    def filter_reserva(reserva: Reserva) -> bool:
        """Filtra as reservas, removendo as reservas do espaço com o código passado

        Args:
            reserva (Reserva): Reserva a ser filtrada

        Returns:
            bool: True se a reserva não for do espaço com o código passado, False caso contrário
        """
        return reserva["codigo-espaco"] != codigo_espaco

    reservas = list(filter(filter_reserva, reservas)) # Filtra as reservas, removendo as reservas do espaço com o código passado
    save_reservas(reservas) # Salva as reservas no arquivo, sobrescrevendo o conte