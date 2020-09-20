import os
# 

files = {
    "pasta_01":{
        "arquivo_01": {
            "nome": "Miguel",
            "idade": 15,
            "altura": 1.85,
            "solteiro": True
        }
    },
    "pasta_02":{
        "arquivo_02": {
            "nome": "Bernardo",
            "idade": 36,
            "altura": 1.65,
            "solteiro": False
        }
    },
    "pasta_03":{
        "arquivo_03": {
            "nome": "Alice",
            "idade": 19,
            "altura": 1.85,
            "solteiro": False
        }
    },
    "pasta_04":{
        "arquivo_04": {
            "nome": "Sophia",
            "idade": 42,
            "altura": 1.56,
            "solteiro": True
        }
    },
    "pasta_05":{
        "arquivo_05": {
            "nome": "Armando",
            "idade": 84,
            "altura": 1.60,
            "solteiro": True
        }
    }
}


texto = """
Esse arquivo pertece ao {nome} o mesmo tem {idade} anos e {altura} de altura e é {relacionamento}
"""

for dado in files:
    

# crie um código pecorra o dict acima.

# 1 - Use a biblioteca "os" para criar a pasta com o mesmo nome da chave da pasta, por exemplo: pasta_01, pasta_02 etc

# 2 - O nome do arquivo deve ser o mesmo nome da chave do arquivo, por exemplo: arquivo_01, arquivo_02.

# 3 - A extensão do arquivo deve ser .txt.

# 4 - No "texto" tem o argumento "relacionamento", esse argumento deve ser formatado, caso a chave "solteiro" seja 
# True o texto deve ser "solteiro", caso seja False deve ser mudado para "casado".

# 5 - Use o texto.format para adicionar os dados dentro do "texto". Por exemplo: texto.format(nome=variavelname) o nome é o argumento dentro da string o variavelname é uma variavel que recebera o nome de dentro do dicionário.