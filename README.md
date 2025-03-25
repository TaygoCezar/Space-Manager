
# Space Manager

Space Manager é uma aplicação para gestão de espaços. Onde é possível cadastrar espaços e realizar reservas.

## Funcionalidades

- Tela Principal
  * Esta tela deve apresentar uma tabela com todos os espaços reservados.
  * A apresentação deve estar ordenada por data da mais recente para a mais distante.
  * Cada reserva deve ter as seguintes informações: código do espaço, nome do espaço, dono da reserva, data e hora início, data e hora fim.
  * Nesta tela deve ter uma ação para criar espaços que irá navegar para a Tela Novo Espaço.
  * Nesta tela deve ter uma ação para criar reserva que irá navegar para a Tela Nova Reserva.
  * Esta tela deve ter um campo de pesquisa que permitirá buscar por prefixo em qualquer campo.
  * A tabela deve também apresentar uma coluna com as ações editar e remover. O link editar deve ir para uma tela de edição com as mesmas regras da tela de cadastro de reserva.

- Tela Novo Espaço
  * Esta tela deve ter os campos código e nome.
  * Os campos são obrigatórios.
  * O campo código deve ser único.
  * Esta tela deve ter uma ação para permitir voltar para a tela principal.

- Tela Nova Reserva
  * Esta tela deve ter os campos: Espaço, dono da reserva, data e hora início e data e hora fim.
  * A campo dono da reserva deve ser uma caixa de seleção para listar os espaços existentes.
  * O cadastro deve validar o início e fim, não permitindo data+hora fim menor que data+hora início.
  * Se a data inicio e fim for no mesmo dia, a reserva deve ser de no mínimo 30 minutos.
  * Não deve ser possível reservar espaço com conflito de horário.
  * Esta tela deve ter uma ação para permitir voltar para a tela principal.

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/TaygoCezar/Space-Manager.git
```

Entre no diretório do projeto

```bash
  cd Space-Manager
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o aplicativo

```bash
  python src/main.py
```
## Autores

- [@murilo-henrique060](https://www.github.com/murilo-henrique060)
- [@nathil](https://www.github.com/nathil)
- [@PedroMends30](https://www.github.com/PedroMends30)
- [@TaygoCezar](https://www.github.com/TaygoCezar)

