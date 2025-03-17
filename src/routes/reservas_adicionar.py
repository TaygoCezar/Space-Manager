import flet as ft
from datetime import datetime as dt

# Validar dados
from utils.validate_reservas import validate_dono, validate_espaco, validate_data, validate_horario, validate_data_hora, validate_intervalo

# Serviços
from services.espacos import get_all
from services.reservas import add_reserva

# Componentes Personalizados
from components.navbar import navbar
from components.form.label import label
from components.form.input import input
from components.form.select import select
from components.form.date_picker import date_picker
from components.form.time_picker import time_picker
from components.form.button_filled import button_filled

def reservas_adicionar(page: ft.Page):
    def is_valid_ref(refs, validate, before=[], params=[]):
        if not all(before):
            return False
        
        error = validate(*params) if params != [] else validate(*[ref.value for ref in refs])
        if error is not None:
            refs[0].error_text = error
            for ref in refs[1:]:
                ref.error_text = " "
            return False
        else:
            for ref in refs:
                ref.error_text = None
            return True
    
    is_intervalo_valid = lambda: is_valid_ref(
        [data_inicio_input, horario_inicio_input, data_termino_input, horario_termino_input],
        validate_intervalo,
        [
            is_valid_ref(
                [data_inicio_input, horario_inicio_input],
                validate_data_hora,
                [
                    is_valid_ref([data_inicio_input], validate_data),
                    is_valid_ref([horario_inicio_input], validate_horario)
                ]
            ),
            is_valid_ref(
                [data_termino_input, horario_termino_input],
                validate_data_hora,
                [
                    is_valid_ref([data_termino_input], validate_data),
                    is_valid_ref([horario_termino_input], validate_horario)
                ]
            )
        ],
        params=[espaco_select.value.split(",")[0], data_inicio_input.value, horario_inicio_input.value, data_termino_input.value, horario_termino_input.value],
    )

    is_dono_valid, reset_dono, dono_input = input("Digite o nome do responsável pela reserva", validate_dono)
    is_espaco_valid, reset_espaco, espaco_select = select("Selecione o espaço", lambda: [ft.DropdownOption(f"{espaco['codigo']},{espaco['nome']}", f"{espaco['codigo']} - {espaco['nome']}") for espaco in get_all()], validate_espaco, handle=lambda e: is_intervalo_valid())
    _, reset_data_inicio, data_inicio_input = date_picker(validate_data, handle=lambda e: is_intervalo_valid())
    _, reset_horario_inicio, horario_inicio_input = time_picker(validate_horario, handle=lambda e: is_intervalo_valid())
    _, reset_data_termino, data_termino_input = date_picker(validate_data, handle=lambda e: is_intervalo_valid())
    _, reset_horario_termino, horario_termino_input = time_picker(validate_horario, handle=lambda e: is_intervalo_valid())

    def init():
        reset_dono()
        reset_espaco()
        reset_data_inicio()
        reset_horario_inicio()
        reset_data_termino()
        reset_horario_termino()

        page.update()

    def handle_save(e):
        if not all([is_dono_valid(), is_espaco_valid(), is_intervalo_valid()]):
            page.update()
            return

        codigo_espaco, nome_espaco = espaco_select.value.split(",")
        add_reserva(
            codigo_espaco=codigo_espaco,
            nome_espaco=nome_espaco,
            dono=dono_input.value,
            inicio=f"{dt.strptime(data_inicio_input.value, "%d/%m/%Y").strftime("%Y-%m-%d")} {horario_inicio_input.value}",
            fim=f"{dt.strptime(data_termino_input.value, "%d/%m/%Y").strftime("%Y-%m-%d")} {horario_termino_input.value}"
        )

        page.open(ft.SnackBar(ft.Text("Reserva salva com sucesso!"), duration=1000)),
        init()

    return init, ft.View(
        controls=[
            navbar("reservas_adicionar"),
            ft.Container    (
                ft.Column([
                    ft.Row([
                        ft.Container(
                            ft.Icon(ft.Icons.ARROW_BACK_OUTLINED, **styles["header-button"]),
                            on_click=lambda e: page.go("reservas")
                        ),
                        ft.Text("Adicionar Reserva", **styles["header"]),
                    ]),

                    ft.Column([label("Dono"), dono_input], **styles["input-field-column"]),
                    ft.Column([label("Espaço"), espaco_select], **styles["input-field-column"]),

                    ft.Row([
                        ft.Row([
                            ft.Column([label("Data de Início"), data_inicio_input], expand=2, **styles["input-field-column"]),
                            ft.Column([label("Horário de Início"), horario_inicio_input], expand=1, **styles["input-field-column"]),
                        ], **styles["inner-row"]),
                        ft.Row([
                            ft.Column([label("Data de Fim"), data_termino_input], expand=2, **styles["input-field-column"]),
                            ft.Column([label("Horário de Fim"), horario_termino_input], expand=1, **styles["input-field-column"])
                        ], **styles["inner-row"])
                    ], **styles["row"]),

                    ft.Row([button_filled("Salvar", ft.Icons.SAVE, handle_save)], **styles["right-row"])
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