import typing as tp
import flet as ft


def validate_ref(refs: list[ft.Ref], validate: tp.Callable, parameters_ref: list[ft.Ref], before: list[tp.Callable] = [], after: list[tp.Callable] = []) -> tp.Callable:
    """Valida a referência

    Valida a referência e atualiza o estado dos componentes.

    Args:
        ref (ft.Ref): Referência a ser validada
        refs (list[ft.Ref]): Lista de referências
        before (list[bool], optional): Validações anteriores. Defaults to [].

    Returns:
        function: Função de validação
    """

    def check_ref() -> bool:
        """Verifica se a referência é válida.
        """
        if not all(list(map(lambda validation: validation(), before))):
            return False
        
        error = validate(*map(lambda ref: ref.current if type(ref.current) is str else ref.current.value , parameters_ref))
        refs[0].current.error_text = error
        for ref in refs[1:]:
            ref.current.error_text = " " if error is not None else None

        refs[0].current.page.update()

        if error is None:
            for checks in after:
                checks()

        return error is None
    
    return check_ref
    