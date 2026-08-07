# Estrutura do Projeto

## main.py

Arquivo principal responsável por iniciar a aplicação e controlar o fluxo de execução.

---

## dados/

Contém os dados principais utilizados pelo sistema, como a lista de temas disponíveis.

---

## docs/

Contém a documentação do projeto.

Arquivos:

- `funcionamento.md`
- `roadmap.md`
- `ideias.md`
- `decisoes.md`

---

## interface/

Responsável pelo gerenciamento da interação com o usuário e armazenamento das variações dos temas.

Exemplos:

- Exibição das opções de variações.
- Controle das escolhas relacionadas às variações.
- Organização das variações disponíveis para cada tema.

---

## json/

Armazena arquivos de configuração utilizados pelo projeto.

Exemplos:

- `config.json` → salva o tema e a variação escolhidos pelo usuário.
- `settings.json` → contém configurações relacionadas ao VS Code.

---

## settings/

Responsável pelo gerenciamento das configurações do ThemeManager e da integração com o VS Code.

Contém as funções responsáveis por:

- Ler o arquivo `config.json`.
- Salvar alterações nas chaves `tema_atual` e `variacao_atual`, mantendo o controle das escolhas realizadas pelo usuário.
- Ler o arquivo `settings.json` do VS Code.
- Salvar alterações nas configurações do editor de código `Visual Studio Code `.
- Alterar o tema do VS Code através da chave `workbench.colorTheme`.
