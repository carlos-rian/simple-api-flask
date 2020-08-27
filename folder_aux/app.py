from flask import Flask, request

# ---------------------------- Instruções ---------------------------------

"""
0 - Verifique se seu ambiente virtual já está ativo, caso não, ative o mesmo usando o comando abaixo.
    source .venv/bin/activate

1 - Suba seu servidor web usando o comando abaixo no terminal.
    python app.py.

2 - Sempre que for preciso executar seu código, chame o "endpoint"/"url" no navegador, usando as urls.
        - se for adicionar o cep, use essa url no navegador.
          127.0.0.1:5000/adicionar/
        - se for ler os ceps, use essa url no navegador.
          127.0.0.1:5000/ler/

3 - Caso queira ver algum resultado no proprio terminal, use o print para mostrar as variaveis.

4 - Caso seu código quebre ao salvar e pare o servidor, corrija o problema e suba novamente o servidor.
"""

app = Flask(__name__)

# ----------------------------- Adendos -----------------------------------
# palavra "pass" deve ser removida das funções, após isso crie seu código.
# não precisa apagar os comentários.


def ler_ceps():
    # Essa função vai ser reponsável por ler todos os ceps do arquivo ceps.txt
    # Após ler, será criado uma lista com todos os CEP dentro do Array do tipo List.
    # Para isso use a função "open" para abrir o arquivo e a função .read para ler o
    # Conteúdo e por fim crie uma variavel que irá receber a lista que você irá gerar com
    # o .split após ler o arquivo.
    # Veja o arquivo ler_escrever_adicionar.py dentro da pasta help.
    try:
        # remova o "pass" e escreva seu código aqui, após ler, converter os dados para lista.
        # retorne o mesmo usando o "return nome_da_variável_lista"
        with open(file="./ceps.txt", mode="r", encoding="utf-8") as abacaxi:
            dados = abacaxi.read().split("\n")
            return dados
    except Exception as error:
        print(error)
        # caso dê erro eu vou retornar uma lista vazia
        return []


@app.route("/ler/")
def ler():
    # logo de cara vou chamar a função que me retorna todos os ceps
    # que estão no meu arquivo ceps.txt, essa função irá me retorna uma lista.
    ceps = ler_ceps()
    # o navegador só entende string/texto lembra, para isso antes de responder o navegador.
    # vamos converter os dados para string. Porém antes de converter vamos verificar se a variável
    # ceps não está vazia, para isso use o if.
    if ceps == []:
        # se for vazio, eu retorno uma mensagem para o navegador, informando.
        return "Olá não tem nenhum cep."
    else:
        # se tiver dados, eu converto para str e retorno para o navegador os ceps.
        return str(ceps)


def adicionar_cep(cep):
    # Essa função irá receber um cep como parâmetro, irá abrir o arquivo de ceps em modo de append.
    # Em seguida vai escrever o cep recebido no final do arquivo.
    # Para isso use a função "open" para abrir o arquivo e a função .write para escrever.
    # Veja o arquivo ler_escrever_adicionar.py dentro da pasta help.
    # Essa função deve retornar um Booleano, caso tenha inserido o cep return True,
    # Caso dê um erro retorne um "False", isso já está implementado.

    try:
        # Seu código irá aqui. Apague o "pass" e digite seu código antes do return True.
        # Caso o seu código esteja correto ele irá retornar o True,
        # Caso dê erro irá printar o erro e retornar False.
        with open(file="./ceps.txt", mode="a", encoding="utf-8") as abacaxi:
            abacaxi.write(f"\n{cep}")
        return True

    except Exception as error:
        # irei printar o erro que aconteceu.
        print(error)
        # caso entre na exception eu retorno um False
        return False


@app.route("/adicionar/")
def adicionar():
    # eu criei a variável meu_cep com o valor do tipo str.
    data = request.args.to_dict()
    meu_cep = data["cep"]
    # estou chamando a função que você irá implementar, para salvar o cep.
    # após executar será retornado um booleano.
    verificador = adicionar_cep(cep=meu_cep)

    # vou verificar se deu certo, se o retorno da função for igual a true é porque foi inserido.
    if verificador == True:
        # eu vou retornar para o navegar uma mensagem.
        return f"Olá, o cep: {meu_cep} foi inserido com sucesso."
    else:
        # eu vou retornar uma mensagem informando que deu erro ao inserir o cep.
        return f"Desculp o cep: {meu_cep} não pode ser inserido."


