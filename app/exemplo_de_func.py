# - como criar uma função em python?
# - no python "não existe" objetos privated, protected etc.
# - tudo no python é objeto, ou seja, nós conseguimos manipular
#   tudo usando métodos dos proprios tipos, por exemplo uma string já
#   tem varios metódos pré prontos, por exemplo o .split que fatia um dado.
#
# - como criar minha primeira função?
# - simples no python existe a palavra reservada chamada "def".
# - essa palavra é o que diferencia uma variavel de uma função/definição.
# - nossa primeira função irá criar somar dois valores.

# def    = definição/função/método
# somar  = nome da definição/função
# x      = primeiro valor valor númerico
# y      = segundo valor númerico
# :      = iniciar novo bloco de código
# return = é uma palavra reservada, usada
#          somente pra especificar o retorno da função.


def subtrair(funcao):
    ...


# def somar(x, y):
#     return x * y


# o python a partir da versão 3.5 lançada em 2016.
# passou a usar uma "linguagem" de anotação de tipos.
# porém isso não quer dizer que as variaveis ou parâmetros,
# não continuaram sendo dinamicos, não é isso. É apenas uma anotação.
# os types hints são apenas uma forma simples de fazer anotações,
# se não faz diferença então? a principal diferença é que podemos saber o tipo
# uma vez que olhamos o tipo. Além de ter maiores vantagens quando usamos um
# editor que irá autocompletar e facilitar o auto preenchimento do dia a dia.

# vamos criar a mesma função de soma com type hint

# : = no caso dos dois pontos a frente de uma variavel é para anotar qual o tipo dela.
#     por exemplo: x: int onde x é a variavel e int é o tipo.
#     também temos o sinal de menos + maior após os parenteses, que informa qual o valor retornado.
#     neste caso a função recebe dois inteiros e retorna um inteiro.


def soma(x: int, y: int) -> int:
    """Essa função soma dois valores inteiro.

    Args:
        x (int): Informe o primeira valor do tipo inteiro
        y (int): Informe o segundo valor do tipo inteiro

    Returns:
        int: Irá retornar o resultado da soma dos dois valores
    """
    return x + y


# implemente o restante da tabuada agora.

# - função de divisão

# - função de multiplicação

# - função de divisão.


# - crie uma função que irá receber uma string e um separador como parâmetro.
# - essa função deve converter a string para lista usando o separador como parâmetro de fatiamento.
# - retorne a lista que foi gerada após converter em string


# - crie uma função que que receba um caminho/path.
# - após receber o path abra o arquivo e leia.
# - com os dados que foram lidos, chame a função que irá converter os dados de string para lista.
# - após receber os dados que foram convertidos para lista.
# - faça um retorno multiplo, ou seja, um retorno com dois valores/variaveis.
# - a primeira variável deve conter o tamanho da lista e a segunda a propria lista.


# - crie uma função que irá lista todos os arquivos que estão dentro da pasta files.
# - retorne essa lista de arquivos em formato list


# - crie uma função que irá chamar todas as funções abaixo em sequência e passando os valores, entre elas.
# - chame a funão que lista os arquivos da pasta files. O retorno deve ser armazenado em uma variavel.
# - chame a função que ler o arquivo, para cada arquivo que foi retornado. O retorno deve ser armazenado em um dict,
#   onde a chave será o nome do arquivo e o valor será o o resultado da função ler arquivo.
# - após coletar todos os dados de todos os arquivos retorne o dict com os valores.


# - crie uma função que irá receber uma lista de valores como string.
# - converta as strings para um dicionário chaveado e altere no dict os valores.
# - com o dicionário pronto, retorne o mesmo como parâmetro.


# - crie uma função que irá receber um dict.
# - chame a função que criar outro dict a partir da lista que será lida no dict recebido.
# - exemplo: irei ler a chave "arquivo_01", com os valores dessa chave, ou seja uma lista eu irei criar um dict.
# - essa função não tem retorno, apenas salva o dict montado como um arquivo .json!


# - crie uma função chama main() essa função é responsável por executar todo o seu programa.
# - essa função será responsável por executar todo o processo desde do inicio.
# - ela deve chamar a função que gera o dicionario.
# - após receber o retorno do dict, passe esses dados para a função que irá salvar os dados.

