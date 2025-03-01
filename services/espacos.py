caminho = "data/espacos.csv"
campos = ["codigo", "nome"]

def criar_arquivo() -> None:
    """Cria o arquivo onde serão armazenados os dados dos espaços.
    """
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(campos) + "\n")

def get_all() -> list:
    """Retorna uma lista com todos os espaços cadastrados.

    Returns:
        list: Lista com todos os espaços cadastrados.
    """

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return [dict(zip(campos, linha.strip().split(","))) for linha in arquivo.readlines()[1:]]
        
        # espacos = []

        # linhas = arquivo.readlines()
        # for linha in linhas[1:]:
        #     linha = linha.strip()
        #     dados = linha.split(",")

        #     espaco = dict(zip(campos, dados))
        #     espacos.append(espaco)
        # return espacos

def inserir_espaco(codigo: str, nome: str) -> None: 
    """Insere um novo espaço no arquivo.

    Args:
        codigo (str): codigo da reserva, não pode ser o código já existente. 
        nome (str): nome do espaço. 

    Raises:
        ValueError: Se o código do espaço já existir.
    """
    # verificar se o código passado já existe, se sim, levanta um value erro. 


    if any([codigo == espaco["codigo"] for espaco in get_all()]):
      raise ValueError(f"O código {codigo} já existe.") 
    


    with open(caminho, "a", encoding="utf-8") as arquivo: 
        arquivo.write(f"{codigo},{nome}\n") 


    # espacos = get_all()
    # for espaco in espacos:
    #     if novo_espaco["codigo"] == espaco["codigo"]:
    #         raise ValueError(f"O código {novo_espaco["codigo"]} já existe.")

    # insere uma nova linha no arquivo de espaços 
    
    # with open(caminho, "a", encoding="utf-8") as arquivo:
    #     novo_espaco = {"codigo": "12", "nome": "sala 2" }
    #     arquivo.write(",".join([novo_espaco[campo] for campo in campos]) + "\n")

        #outros modo de fazer a linha 54 
        #nova_linha = f"{novo_espaco["codigo"]},{novo_espaco["nome"]}\n"
        # nova_linha = novo_espaco["codigo"] + "," + novo_espaco["nome"] + "\n" 
        # arquivo.write(nova_linha)  
        # arquivo.write(",".join(espaco.values()) + "\n")


    inserir_espaco("0", "mesa 9")