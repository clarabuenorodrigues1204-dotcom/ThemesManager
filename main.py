from os import system
system('cls')

from time import sleep
import dados.temas as temas
import json
from interface import interface_variacao

titulo = "THEMES MANAGER" #Mostra o título

print(f'{titulo:=^40}')

#Escolha do tema
for i, tema in enumerate(temas.temas, start=1):#Mostra o tema
    print(f'[{i}] - {tema}')

opcao_usuario = int(input('\nQual é a opção desejada? '))

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
     
#Escolha da variação do tema

variacao_escolhida = interface_variacao.escolha_variacao(tema_escolhido)
print(f'Variação escolhida: {variacao_escolhida}')
print('Aplicando....')
sleep(1)