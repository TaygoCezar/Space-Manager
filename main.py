
#vou criar um universo repleto de dor e sofrimento. 
#- Ass, Nath. 


import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Tabela Bonita para o Professor Hidaka"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT  # Modo claro
    page.update()

    # Criando uma tabela estilizada
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)),
            ft.DataColumn(ft.Text("Nome", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)),
            ft.DataColumn(ft.Text("Nota", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("João Silva")),
                    ft.DataCell(ft.Text("9.5")),
                ],
                color=ft.colors.GREY_200,  # Cor de fundo da linha
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("2")),
                    ft.DataCell(ft.Text("Maria Oliveira")),
                    ft.DataCell(ft.Text("8.7")),
                ],
                color=ft.colors.WHITE,  # Cor de fundo da linha
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("3")),
                    ft.DataCell(ft.Text("Carlos Souza")),
                    ft.DataCell(ft.Text("7.8")),
                ],
                color=ft.colors.GREY_200,  # Cor de fundo da linha
            ),
        ],
        border=ft.border.all(2, ft.colors.BLUE_800),  # Borda da tabela
        border_radius=10,  # Borda arredondada
        heading_row_color=ft.colors.BLUE_100,  # Cor de fundo do cabeçalho
        heading_text_style=ft.TextStyle(color=ft.colors.BLUE_800, weight=ft.FontWeight.BOLD),
        divider_thickness=1,  # Espessura da linha divisória
        horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_400),  # Linhas horizontais
        vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_400),  # Linhas verticais
    )

    # Adicionando a tabela à página
    page.add(table)

# Executar o aplicativo
ft.app(target=main)
