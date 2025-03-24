import flet as ft

# Serviços
from services.reservas_service import get_reserva_by_codigo, update_reserva
from services.espacos_service import get_all_espacos

# Controllers
from controllers.reservas_controller import validate_dono, validate_espaco, validate_data, validate_horario, validate_data_hora, validate_intervalo

# Utils
from utils.validation_util import validate_ref
from utils.date_util import convert_str_date_to_format, convert_format_date_to_str

# Componentes Personalizados
from components.navbar import navbar
from components.form.label import label
from components.form.input import input
from components.form.select import select
from components.form.date_picker import date_picker
from components.form.time_picker import time_picker
from components.form.button_filled import button_filled

def reservas_editar(page: ft.Page):
    """Página de editar reserva

    Página para editar uma reserva existente.

    Args:
        page (ft.Page): Página atual

    Returns:
        function: Função de inicialização   
        ft.View: Página de editar reserva
    """
    # Inicialização
    def init(codigo: str):
        current_codigo_ref.current = codigo

        reserva = get_reserva_by_codigo(current_codigo_ref.current)

        if reserva is None:
            page.go("reservas")
            page.open(ft.SnackBar(ft.Text("Reserva não encontrada."), duration=1000))
            return

        espaco_ref.current.options = list(map(lambda espaco: ft.DropdownOption(f"{espaco['codigo']},{espaco['nome']}", f"{espaco['codigo']} - {espaco['nome']}"), get_all_espacos()))

        for ref, value in zip(
            [dono_ref, espaco_ref, data_inicio_ref, horario_inicio_ref, data_termino_ref, horario_termino_ref],
            [reserva["dono"], f"{reserva['codigo-espaco']},{reserva['nome-espaco']}"] + list(convert_format_date_to_str(reserva["inicio"])) + list(convert_format_date_to_str(reserva["fim"]))
        ):
            ref.current.value = value
            ref.current.error_text = None

        page.update()

    # Referências
    current_codigo_ref = ft.Ref[str]()
    dono_ref = ft.Ref[ft.TextField]()
    espaco_ref = ft.Ref[ft.DropdownM2]()
    data_inicio_ref = ft.Ref[ft.DatePicker]()
    horario_inicio_ref = ft.Ref[ft.TimePicker]()
    data_termino_ref = ft.Ref[ft.DatePicker]()
    horario_termino_ref = ft.Ref[ft.TimePicker]()
    
    # Validações
    check_dono = validate_ref([dono_ref], validate_dono, [dono_ref])
    check_espaco = validate_ref([espaco_ref], validate_espaco, [espaco_ref], after=[lambda: check_interval()])
    check_interval = validate_ref(
        [data_inicio_ref, horario_inicio_ref, data_termino_ref, horario_termino_ref],
        validate_intervalo,
        [espaco_ref, data_inicio_ref, horario_inicio_ref, data_termino_ref, horario_termino_ref, current_codigo_ref],
        [
            validate_ref(
                [data_inicio_ref, horario_inicio_ref],
                validate_data_hora,
                [data_inicio_ref, horario_inicio_ref],
                [
                    validate_ref([data_inicio_ref], validate_data, [data_inicio_ref]),
                    validate_ref([horario_inicio_ref], validate_horario, [horario_inicio_ref])
                ],
            ),
            validate_ref(
                [data_termino_ref, horario_termino_ref],
                validate_data_hora,
                [data_termino_ref, horario_termino_ref],
                [
                    validate_ref([data_termino_ref], validate_data, [data_termino_ref]),
                    validate_ref([horario_termino_ref], validate_horario, [horario_termino_ref])
                ],
            )
        ]
    )

    # Eventos
    def save(e: ft.TapEvent):
        """Salva a reserva
        """
        if not all([check_dono(), check_espaco(), check_interval()]):
            page.update()
            return
        
        codigo_espaco, nome_espaco = espaco_ref.current.value.split(",")
        update_reserva(
            codigo=current_codigo_ref.current,
            codigo_espaco=codigo_espaco,
            nome_espaco=nome_espaco,
            dono=dono_ref.current.value,
            inicio=f"{convert_str_date_to_format(data_inicio_ref.current.value)} {horario_inicio_ref.current.value}",
            fim=f"{convert_str_date_to_format(data_termino_ref.current.value)} {horario_termino_ref.current.value}"
        )
        
        page.open(ft.SnackBar(ft.Text("Reserva salva com sucesso!"), duration=1000))
        init(current_codigo_ref.current)

    return init, ft.View(
        controls=[
            navbar("reservas_editar"),
            ft.Container    (
                ft.Column([
                    ft.Row([
                        ft.Container(
                            ft.Icon(ft.Icons.ARROW_BACK_OUTLINED, **styles["header-button"]),
                            on_click=lambda e: page.go("reservas")
                        ),
                        ft.Text("Editar Reserva", **styles["header"]),
                    ]),

                    ft.Column([label("Dono"), input("Digite o nome do responsável pela reserva", dono_ref, check_dono)], **styles["input-field-column"]),
                    ft.Column([label("Espaço"), select("Selecione o espaço", espaco_ref, check_espaco)], **styles["input-field-column"]),

                    ft.Row([
                        ft.Row([
                            ft.Column([label("Data de Início"), date_picker(data_inicio_ref, check_interval)], expand=2, **styles["input-field-column"]),
                            ft.Column([label("Horário de Início"), time_picker(horario_inicio_ref, check_interval)], expand=1, **styles["input-field-column"]),
                        ], **styles["inner-row"]),
                        ft.Row([
                            ft.Column([label("Data de Fim"), date_picker(data_termino_ref, check_interval)], expand=2, **styles["input-field-column"]),
                            ft.Column([label("Horário de Fim"), time_picker(horario_termino_ref, check_interval)], expand=1, **styles["input-field-column"])
                        ], **styles["inner-row"])
                    ], **styles["row"]),

                    ft.Row([button_filled("Salvar", ft.Icons.SAVE, save)], **styles["right-row"])
                ], **styles["main-row"]),
                **styles["main-container"]
            )
        ],
        **styles["body"]
    )

styles = {
    "body": {
        "padding": ft.padding.all(0),
    },

    "main-container": {
        "padding":ft.padding.symmetric(25,25) 
    },

    "main-row": {
        "spacing": 20
    },

    "header-button": {
        "color": "#003565",
    },

    "header": {
        "color": "#003565", 
        "font_family": "Saira Extra Condensed - Bold",
        "size": 25
    },

    "input-field-column": {
        "spacing": 5
    },

    "row": {
        "spacing": 20,
        "vertical_alignment": ft.CrossAxisAlignment.START
    },
    "inner-row": {
        "spacing": 10,
        "vertical_alignment": ft.CrossAxisAlignment.START,
        "expand": 2
    },

    "right-row": {
        "alignment": ft.MainAxisAlignment.END
    }
}