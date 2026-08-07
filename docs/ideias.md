# Ideias do Projeto

Arquivo destinado para registrar ideias futuras, melhorias e possíveis funcionalidades para o ThemeManager.

---

## Novas funcionalidades

### Indexador automático de temas

- Procurar automaticamente os temas instalados no VS Code.
- Identificar extensões de temas.
- Exibir apenas temas disponíveis no sistema.
- Evitar que o usuário precise cadastrar temas manualmente.

---

### Interface gráfica

Criar uma interface visual para substituir o terminal.

Possíveis tecnologias:

- Tkinter
- CustomTkinter
- PySide/PyQt

Possibilidades:

- Lista de temas com pré-visualização.
- Botão para aplicar tema.
- Configuração de preferências.

---

### Integração com VS Code

Transformar o projeto em uma extensão oficial do VS Code.

Possíveis recursos:

- Alterar tema pelo Command Palette.
- Criar atalhos para troca rápida.
- Sincronizar configurações.

---

### Sistema de favoritos

Permitir que o usuário marque temas favoritos.

Exemplo:

- ⭐ Dracula
- ⭐ GitHub Theme
- ⭐ Cyberpunk Theme

---

### Backup e restauração

Criar um sistema para salvar configurações antes de alterar o tema.

Exemplo:

backup/
├── settings_backup.json
└── config_backup.json


Funcionalidades:

- Restaurar configurações anteriores.
- Criar pontos de restauração.

---

### Configuração personalizada

Permitir que o usuário escolha:

- Tema padrão.
- Variação inicial.
- Local do arquivo settings.json.
- A frequência que será realizado o backup.

---

## Melhorias técnicas

### Organização do código

- Separar melhor responsabilidades.
- Criar classes para gerenciamento de temas.
- Melhorar tratamento de erros.

---

### Testes automatizados

Adicionar testes para:

- Leitura dos arquivos JSON.
- Validação de temas.
- Alteração das configurações.

---

### Logs

Criar um sistema de registros:

Exemplo:

[INFO] Tema alterado com sucesso.
[ERROR] Tema não encontrado.

## Ideias futuras

- Criar instalador do programa.
- Criar versão multiplataforma.
- Adicionar suporte para outros editores de código.
- Criar uma página/documentação do projeto.