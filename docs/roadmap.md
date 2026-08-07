# Roadmap - ThemeManager

Plano de evolução do projeto e suas principais funcionalidades.

---

# Versão 0.1 — Protótipo inicial

## Objetivo:

Criar a primeira versão funcional do gerenciador de temas.

## Concluído:

* Criar painel de interação no terminal.
* Exibir lista de temas disponíveis.
* Permitir escolha do usuário.
* Validar escolha do usuário.
* Implementar sistema de variações de temas.
* Armazenar tema e variação escolhidos em arquivo JSON.

---

# Versão 0.2 — Integração com VS Code

## Objetivo:

Permitir que o programa altere automaticamente as configurações do VS Code.

## Em desenvolvimento:

* Ler o arquivo `settings.json`.
* Localizar a chave `workbench.colorTheme`.
* Aplicar o tema escolhido automaticamente.
* Salvar alterações no arquivo de configuração.
* Criar sistema de backup das configurações originais.

---

# Versão 0.3 — Organização e qualidade do código

## Objetivo:

Melhorar a estrutura interna do projeto e facilitar sua manutenção.

## Planejado:

* Organizar melhor a arquitetura do projeto.
* Separar responsabilidades entre módulos.
* Padronizar nomes de arquivos e variáveis em inglês.
* Melhorar tratamento de erros.
* Criar testes automatizados.
* Melhorar documentação.

---

# Versão 0.4 — Indexador automático de temas

## Objetivo:

Detectar automaticamente os temas instalados no VS Code.

## Planejado:

* Utilizar `pathlib` para acessar diretórios.
* Localizar extensões instaladas.
* Ler arquivos de configuração das extensões.
* Identificar extensões que possuem temas.
* Criar lista automática de temas disponíveis.

---

# Versão 0.5 — Interface gráfica

## Objetivo:

Substituir o terminal por uma interface visual.

## Planejado:

* Criar interface gráfica.
* Exibir temas disponíveis visualmente.
* Permitir aplicação de temas por botões.
* Melhorar experiência do usuário.

---

# Versão 1.0 — Aplicação completa

## Objetivo final:

Transformar o ThemeManager em uma ferramenta completa para gerenciamento de temas do VS Code.

## Planejado:

* Sistema completo de gerenciamento de temas.
* Interface amigável.
* Backup e restauração de configurações.
* Configurações personalizadas.
* Preparação para possível extensão do VS Code.
* Publicação da versão estável.
