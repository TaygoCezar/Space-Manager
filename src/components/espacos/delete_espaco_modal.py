import typing as tp
import flet as ft

# Servicos
from services.espacos_service import delete_espaco


def delete_espaco_modal(codigo: str, update_table: tp.Callable) -> ft.AlertDialog:
    """Modal para deletar um espaço.

    Args:
        codigo (str): Código do espaço.
        update_table (Callable): Função para atualizar a tabela de espaços.

    Returns:
        AlertDialog: Modal de confirmação
    """
    # Referências
    modal_ref = ft.Ref[ft.AlertDialog]()

    # Eventos
    def close_modal(e):
        e.control.page.close(modal_ref.current)

    def delete(e):
        delete_espaco(e.control.data)
        close_modal(e)
        update_table()
        e.control.page.open(ft.SnackBar(ft.Text("Espaço deletado com sucesso!"), duration=1000))

    # Componente
    return ft.AlertDialog(
        ref=modal_ref,
        modal=True,
        title=ft.Text("Deletar Reserva", **styles["title"]),
        content=ft.Column([
            ft.Text("Tem certeza que deseja deletar esta reserva?", **styles["description"]),
            ft.Text("(Esta ação também deletará todas as reservas cadastradas neste espaço!)", **styles["description-warning"])
        ], **styles["modal-column"]),
        actions=[
            ft.FilledButton("Cancelar", on_click=close_modal, **styles["filled-button"]),
            ft.FilledButton("Deletar", data=codigo, on_click=delete, **styles["filled-button"])
        ]
    )


# Estilos
styles = {
    "modal-column": {
        "tight": True,
        "spacing": 0
    },
    "title": {
        "color": "#003565",
        "size": 22,
        "weight": "bold"
    },
    "description": {
        "color": "#003565",
        "size": 16
    },
    "description-warning": {
        "color": "#6A1414",
        "size": 14
    },
    "filled-button": {
        "bgcolor": "#003565",
        "style": ft.ButtonStyle(
            padding= ft.padding.symmetric(18, 20),
            shape=ft.RoundedRectangleBorder(9),
            text_style=ft.TextStyle(
                size=16
            )
        )
    },
}