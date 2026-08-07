def escolha_tema(interface_temas):
    titulo = "THEMES MANAGER"
    print(f'{titulo:=^40}')

    for i, tema in enumerate(interface_temas, start=1):
        print(f'[{i}] - {tema}')

    while True:
        try:
            opcao_usuario = int(input('\nQual é a opção desejada? '))
            print("-" * 40)
            
            if opcao_usuario in range(1, len(interface_temas) + 1):
                
                tema_escolhido = list(interface_temas)[opcao_usuario - 1]
                return tema_escolhido
            else:
                print('Opção inválida!')
                
        except ValueError:
            print('Digite apenas números.')