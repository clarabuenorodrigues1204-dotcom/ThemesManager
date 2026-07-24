from os import system
system('cls')

import ThemesManager.temas as temas
from time import sleep
import json
import ThemesManager.interface_variacao as interface_variacao

arquivo = open("config.json" , "r") #Python encontra o arquivo e abre ele
config = json.load(arquivo) #faz a conversão de json para python para que o python consiga manipular
arquivo.close()

print(config)

titulo = "GERENCIADOR DE TEMAS" #Mostra o título

print(f'{titulo:=^40}')

for i, tema in enumerate(temas.temas, start=1): #Mostra o tema
    print(f'[{i}] - {tema}')
    
opcao_usuario = int(input('\nQual é a opção desejada? ')) #O usuário faz a escolha desejada

tema_escolhido = list(temas.temas.keys())[opcao_usuario -1]

variacoes = temas.temas[tema_escolhido]
variacao_escolhida = interface_variacao.escolher_variacao(tema_escolhido)

print(f'Variação escolhida: {variacao_escolhida}')
print('Aplicando...')

config["tema_atual"] = variacao_escolhida
sleep (1)

arquivo = open("config.json" , "w")
json.dump(config, arquivo , indent=4)
arquivo.close()

arquivo = open("C:\\Users\\clara\\AppData\\Roaming\\Code\\User\\settings.json" ,"r+")
settings = json.load(arquivo)
settings["workbench.colorTheme"] = variacao_escolhida
arquivo.seek(0)
arquivo.truncate()
json.dump(settings , arquivo)

print(config["tema_atual"]) #Mostra o tema atual do usuário
