"""
Vamos criar um banco de dados usando apenas python.
Para isso iremos usar um dicionário que armazena dicionários.
O nosso dicionário iniciará vazio.
"""

# essa é uma das formas de declarar um dicionário. A outra seria colocando apenas chaves {}.
# desde do python 3.6 nós temos a opção de fazer types hints, e o que seria isso?
# o python é uma linguagem com tipagem dinâmica, quando o código começa a ficar muito grande
# as vezes é dificil saber qual o tipo que aquela variável X tem. Então uma forma mais simples é
# adicionar uma type hint ou type annotation, que basicamente é falar o tipo da variável após a declaração.
# para isso usamos dois pontos (:) e falamos qual é o tipo.
banco_de_dados: dict = dict()
# Nosso dict, precisa receber uma chave de ID do tipo Int automaticamente, quando inserirmos qualquer dado no mesmo.

"""
Nós iremos criar um banco de dados bem simples, para isso precisaremos criar algumas validações, 
ou até mesmo implementação que façam isso automaticamente.
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
def add_value(id: int, value: dict) -> str:
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
