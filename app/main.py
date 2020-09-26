from flask import Flask, request


app = Flask(__name__)
# por padrão minha url vai ser 127.0.0.1:5000 ou localhost:5000

# exemplo simples usando somente o caminho padrão/host.
@app.route("/")
def home():
    return "está é uma página web"


# exemplo de chamada usando caminho/path
@app.route("/caminho")
def caminho():
    return ("não foi possivel te atender senhor", 202)


# exemplo de chamada usando caminho/path dinamico
@app.route("/caminho/<dinamico>/")
def dinamico(dinamico):
    return (f"Eu recebi esse parâmetro dinamicamente: {dinamico}", 200)


# exemplo de chamada usando caminho/path argumentos
@app.route("/argumentos/")
def argumentos():
    args = dict(request.args)
    return (f"Eu recebi tudo isso: {args}", 200)


# exemplo de chamada usando caminho/path add dados ao header HTML
@app.route("/header/")
def header():
    return (f"<h1> Olá Carlos </h1>", 200, {"Content-type": "text/html"})


# exemplo de chamada usando caminho/path add dados ao header json
@app.route("/header-como-json/")
def json():
    return ({"nome": "carlos"}, 200, {"Content-type": "application/json"})


""" Desafios da semana """

""" primeira questão """
# crie um novo endpoint que receba um cep como argumento na url, exemplo: url.com/?cep=12345678
# verifique se é um cep valido(se tem 8 digitos, se tem somente números),
# caso seja crie ou adicione esse cep em um arquivo .txt e retorne a seguintes informações.
# mensagem: {"message":"o cep {cep} foi inserido com sucesso"}
# código de status: 201
# headers: do tipo application json
# caso não seja valido. retorne uma mensagem semelhante a de sucesso só que informando o erro
# com código de status 400 e o header também como json.


""" segunda questão """
# crie um novo endpoint que receba um cep dinamicamente no path/caminho da url e receba isso como parâmetro da função.
# após receber esses parâmetro de cep verifique se o mesmo já está no arquivo de ceps.
# caso esteja, retorne uma mensagem informando.
# mensagem: {"message":"o cep {cep} está cadastrado."}
# código de status: 200
# headers: do tipo application json
# caso não esteja, retorne uma mensagem informando que não foi encontrado e retorne 400 e o header como application json


# como retornar html ao invés de uma string ou array.
from flask import render_template


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/for/<nome>")
def index_for(nome):
    title = "olá eu sou o {nome}"
    users = [{"username": nome}]
    return render_template("for.jinja", title=title, users=users)


@app.route("/if/<nome>")
def index_if(nome):
    title = "olá eu sou o {nome}"
    users = [{"username": nome}]
    return render_template("if.jinja", title=title, users=users)

