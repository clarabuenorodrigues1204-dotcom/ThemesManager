from os import system
system('cls')

from time import sleep
import dados.temas as temas
import json
from interface import interface_variacao
from settings.save_config import salvar_config

titulo = "THEMES MANAGER" #Mostra o título

print(f'{titulo:=^40}')

#Menu de opções de tema
for i, tema in enumerate(temas.temas, start=1):#Mostra o tema
    print(f'[{i}] - {tema}')

#Entrada/escolha do usuário
opcao_usuario = int(input('\nQual é a opção desejada? '))
print( "-" * 40)

#Validação da escolha do tema
while True:   
    
    try:
        if opcao_usuario in range(1, len(temas.temas) + 1):
            
            break
        
        else:
            print('Opção inválida!')
            opcao_usuario = int(input('Digite uma opção válida '))
            
    except ValueError:
        print("Digite apenas números.")
        
tema_escolhido = list(temas.temas)[opcao_usuario -1]   
     

#Alteração do arquivo config.json

variacao_escolhida = interface_variacao.escolha_variacao(tema_escolhido)
print( "-" * 40)
print(f'Variação escolhida: {variacao_escolhida}')
print('Aplicando....')
sleep(1)


salvar_config(tema_escolhido , variacao_escolhida)

