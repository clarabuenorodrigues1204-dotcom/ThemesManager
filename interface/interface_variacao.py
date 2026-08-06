import json
from dados import temas

def escolha_variacao(tema_escolhido):

    with open("interface/interface_variacao.json" , "r" , encoding= "utf-8") as arquivo:
        interface_variacao = json.load(arquivo)
        variacoes_disponiveis = interface_variacao[tema_escolhido]
        
        for indice, variacao in enumerate(variacoes_disponiveis, start=1):
            print(f'{indice} - {variacao}')
            
    while True:
        try:
            print( "-" * 40)
            variacao = int(input('Escolha uma variação de tema: '))
            
            if 1 <= variacao <= len(variacoes_disponiveis):
                return variacao
        
            print('Opção Inválida!')
            
        except ValueError:
            print('Digite apenas números!')

            
        