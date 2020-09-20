dictionare = {
    1: {"nome": "Miguel", "idade": 15, "altura": 1.85, "solteiro": True},
    2: {"nome": "Bernardo", "idade": 36, "altura": 1.65, "solteiro": False},
    3: {"nome": "Alice", "idade": 19, "altura": 1.85, "solteiro": False},
    4: {"nome": "Sophia", "idade": 42, "altura": 1.56, "solteiro": True},
    5: {"nome": "Armando", "idade": 84, "altura": 1.60, "solteiro": True},
}

from pprint import pprint

# 01
# CRIE UM CÓDIGO QUE REMOVA DO dictionare ONDE ID/CHAVE SEJA IGUAL 4.
retorno = dictionare.pop(4)
# 02
# CRIE UM CÓDIGO QUE ADICIONE OU ATUALIZE UM REGISTRO NO dictionare.
dictionare.update({4: retorno})
# 03
# CRIE UM CÓDIGO QUE PRINT TODAS AS CHAVES DO dictionare.
dictionare.keys()
# 04
# CRIE UM CÓDIGO QUE PRINT A MENOR CHAVE DO dictionare.
chaves = list(dictionare.keys())
minimo = chaves[0]
for i in dictionare.keys():
    if minimo > i:
        minimo = i
print(minimo)

# 05
# CRIE UM CÓDIGO QUE PRINT A MAIOR CHAVE DO dictionare.
chaves = list(dictionare.keys())
maximo = chaves[0]
for i in dictionare.keys():
    if maximo < i:
        maximo = i
print(maximo)

