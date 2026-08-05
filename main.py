from os import system
system('cls')

from time import sleep
import dados.temas as temas
import json

titulo = "THEMES MANAGER" #Mostra o título

print(f'{titulo:=^40}')

for i, tema in enumerate(temas.temas, start=1):#Mostra o tema
    print(f'[{i}] - {tema}')

opcao_usuario = int(input('\nQual é a opção desejada? '))

while True:   
    
    try:
        if opcao_usuario in range(1, len(temas.temas) + 1):
            
            break
        
        else:
            print('Opção inválida!')
            opcao_usuario = int(input('Digite uma opção válida '))
            
    except ValueError:
        print("Digite apenas números.")

print('Aplicando....')
sleep(1)