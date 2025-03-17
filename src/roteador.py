import flet as ft
from utilidades import rota

# Páginas do aplicativo


def inicializar(p: ft.Page) -> None:
    """Inicializa o roteador e carrega as rotas da aplicação.

    Args:
        p (ft.Page): Objeto da página.
    """

    global page, rotas
    
    page = p
    rotas = carregar_rotas()


def carregar_rotas() -> dict:
    """Carrega as rotas da aplicação.

    Returns:
        dict: Dicionário de rotas.
    """

    paginas = []
    return{
        nome: {
            "ao_iniciar": ao_iniciar,
            "pagina": pagina
        } for nome, ao_iniciar, pagina in map(lambda pagina: pagina(), paginas)
    }


def ao_navegar(e: ft.RouteChangeEvent) -> None:
    """Gerencia a navegação entre as páginas da aplicação.

    Args:
        e (ft.RouteChangeEvent): Evento de mudança de rota.

    Raises:
        ValueError: Rota não encontrada.
    """

    nome, parametros = rota.decompor(e.route)

    if nome not in rotas:
        raise ValueError(f"Rota {nome} não encontrada.")

    page.views.clear() # Limpa as views da página
    rotas[nome]["ao_iniciar"](**parametros) # Chama a função ao_iniciar da página e passa os parâmetros
    page.views.append(rotas[nome]["pagina"]) # Adiciona a view da página
    page.update() # Atualiza a página