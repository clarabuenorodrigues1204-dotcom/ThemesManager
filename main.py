from os import system
system('cls')

import dados.temas as temas
import json

titulo = "THEMES MANAGER" #Mostra o título

print(f'{titulo:=^40}')

for i, tema in enumerate(temas.temas, start=1):#Mostra o tema
    print(f'[{i}] - {tema}')

opcao_usuario = int(input('\nQual é a opção desejada? '))

while opcao_usuario < 1 or opcao_usuario >(len(temas.temas)):
    print('Opção inválida!')
    opcao_usuario = int(input('Escolha uma opção válida: '))
