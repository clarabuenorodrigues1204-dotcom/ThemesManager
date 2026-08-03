from os import system
system('cls')

import dados.temas as temas
import interface.interface_variacao as interface_variacao
import json

arquivo = open("json/config.json" , "r")
config = json.load(arquivo) #faz a conversão de json para python para que o python consiga manipular
arquivo.close()

print(config)

titulo = "THEMES MANAGER" #Mostra o título

print(f'{titulo:=^40}')

for i, tema in enumerate(temas.lista_temas, start=1):#Mostra o tema
    print(f'[{i}] - {tema}')

opcao_usuario = int(input('\nQual é a opção desejada? '))

