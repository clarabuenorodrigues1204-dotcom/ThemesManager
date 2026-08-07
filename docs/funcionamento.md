# Funcionamento

O usuário inicia o programa através do arquivo `main.py`, que controla o fluxo principal da aplicação.

## Funcionamento do código - v1.0

O fluxo de execução do programa ocorre da seguinte forma:

1. O programa define o título da aplicação.
2. O título é exibido de forma formatada no terminal.
3. O sistema percorre a lista de temas disponíveis.
4. Cada tema é exibido com um número de identificação.
5. O usuário informa o tema desejado.
6. O sistema realiza a validação da escolha do usuário.
7. Após a validação, o programa busca o tema correspondente na lista de dados.
8. O sistema exibe o menu de variações disponíveis para o tema selecionado.
9. O programa consulta o arquivo JSON responsável por armazenar as variações dos temas.
10. O usuário seleciona uma variação disponível.
11. O sistema valida a escolha da variação.
12. O tema e a variação escolhidos são armazenados no arquivo `config.json`.

## Responsabilidades do `main.py`

O arquivo `main.py` é responsável por:

* Iniciar a aplicação.
* Controlar o fluxo principal do programa.
* Solicitar as escolhas do usuário.
* Chamar os módulos responsáveis pela interface e configurações.
* Salvar as informações escolhidas pelo usuário.

## Fluxo resumido:

```
main.py
   ↓
Exibição dos temas
   ↓
Escolha do usuário
   ↓
Validação
   ↓
Seleção da variação
   ↓
Validação
   ↓
Salvamento no config.json
```

