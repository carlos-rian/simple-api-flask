"""
O modulo json é uma biblioteca  padrão do python.
A mesma tem como objetivo principal converter arrays em string e vice-versa
"""
import json


# TODO -> (PARA FAZER) -  CRIE UMA FUNÇÃO PARA ABRIR O ARQUIVO
def open_db(mode: str) -> open:
    """
    Essa função irá abrir o arquivo e retorna o arquivo aberto.
    """


# TODO -> (PARA FAZER) -  CRIE UMA FUNÇÃO PARA FECHAR O ARQUIVO
def close_db(file: open) -> None:
    """
    Essa função irá fechar o arquivo.
    """


# TODO -> (PARA FAZER) -  CRIE UMA FUNÇÃO LER O ARQUIVO
def read_db() -> dict:
    """
    Leia o arquivo de texto, converta o mesmo para dicionário, feche o arquivo e retorne o dict.
    """


# TODO -> (PARA FAZER) -  CRIE UMA FUNÇÃO IRÁ ESCREVER OS DADOS NO ARQUIVO
def write_db(value: dict) -> None:
    """
    Essa função deve criar o arquivo caso não exista, converter o dict recebido para str e 
    escrever os dados convertidos no arquivo.
    """


# TODO -> (PARA FAZER) - CRIE UMA FUNÇÃO PARA GERAR UM ID
def get_next_id() -> int:
    """
    Nosso primeiro objetivo é criar uma função que verifique qual o último ID no dicionário e retornar qual o próximo.
    """


# TODO -> (PARA FAZER) - CRIE UMA FUNÇÃO QUE RETORNE OS DADOS A PARTIR DO ID.
def get_value(id: int) -> dict:
    """
    Crie uma função que verifique se existe um id existe no banco e retorne o valor.
    """


# TODO -> (PARA FAZER) - CRIE UMA FUNÇÃO QUE IRÁ ADICIONAR UM REGISTRO.
def add_value(id: int, values: dict) -> str:
    """
    Segundo, precisamos adiconar dentro do banco de dados um novo dict que a chave será gerada pela função anterior.
    Por exemplo: {ID: {"nome": "carlos", "idade": 26, "altura": 1.77}}
    """


# TODO -> (PARA FAZER) - CRIE UMA FUNÇÃO QUE IRÁ REMOVER UM REGISTRO.
def remove_value(id: int) -> str:
    """
    Terceiro, precisamos implementar um método que irá receber um ID, após receber o mesmo nós removemos de dentro do 
    banco de dados.
    """


# TODO -> (PARA FAZER) - CRIE UMA FUNÇÃO IRÁ FAZER UPDATE DE UM REGISTRO.
def update_value(id: int, value: dict) -> str:
    """
    Quanto, precisamos fazer update em um registro no nosso banco de dados. Para isso essa função precisa de duas 
    informações, primeiro o ID e depois o dado que será passado. Caso o id não exista teremos que falar que o dado não
    existe no nosso banco de dados.
    """
