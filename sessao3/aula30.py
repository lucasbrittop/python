"""
constantes = "variavis que não vão mudar
muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual
local_carro = 61 #km atual

RADAR_1 = 60 #velocidade max do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #a distancia onde o radar pega

if velocidade > RADAR_1:
    print('velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('multado')