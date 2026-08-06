import json

def salvar_config(tema_escolhido , variacao_escolhida):
    with open("json/config.json" , "r" , encoding= "utf-8") as arquivo:
        config = json.load(arquivo)
        
        config["tema_atual"] = tema_escolhido
        config["variacao_atual"] = variacao_escolhida
        
    with open("json/config.json", "w" , encoding="utf-8") as arquivo:
        json.dump(config, arquivo , indent=4, ensure_ascii= False)   
    