import json

#Traz os valores de conversão de cada unidade
with open('modulos/unidades.json', 'r', encoding="utf8") as arquivo:
    unidades = json.load(arquivo)


#Função para converter unidades
def converter(valor, unidade_origem, unidade_destino):
    
    for unidade, medidas in unidades.items():
        if (unidade_origem in medidas and unidade_destino in medidas) and unidade != "temperatura":
            conversao = (valor / medidas[unidade_origem]) * medidas[unidade_destino]
            return round(conversao, 2)

        elif unidade == "temperatura":
            return converter_temperatura(valor, unidade_origem, unidade_destino)

    return None


#Função para converter temperatura
def converter_temperatura(valor, unidade_origem, unidade_destino):
    
    if unidade_origem == "C":
        if unidade_destino == "F":
            return round((valor * 9 / 5) + 32, 2)
        elif unidade_destino == "K":
            return round(valor + 273.15, 2)
        else:
            return None
            
    elif unidade_origem == "F":
        if unidade_destino == "C":
            return round((valor - 32) * 5 / 9, 2)
        elif unidade_destino == "K":
            return round((valor - 32) * 5 / 9 + 273.15, 2)
        else:
            return None
            
    else:
        if unidade_destino == "C":
            return round(valor - 273.15, 2)
        elif unidade_destino == "F":
            return round((valor - 273.15) * 9 / 5 + 32, 2)
        else:
            return None
