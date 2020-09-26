from flask import Flask, request, render_template


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
    if dinamico == "qualquercoisa":
        return (f"Não existe: {dinamico}", 404)
    return (f"Eu recebi esse parâmetro dinamicamente: {dinamico}", 200)
    (str, dict, list, numbers)


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
# crie um novo endpoint que receba um cep como argumento na url, exemplo: url.com/?cep=12345678cep2=296656
# verifique se é um cep valido(se tem 8 digitos, se tem somente números),
# caso seja crie ou adicione esse cep em um arquivo .txt e retorne a seguintes informações.
# mensagem: {"message"":o cep {cep} foi inserido com sucesso"}
# código de status: 201
# headers: do tipo application json
# caso não seja valido. retorne uma mensagem semelhante a de sucesso só que informando o erro
# com código de status 400 e o header também como json.
@app.route("/cep/")
def cep():
    args = dict(request.args)
    if "cep" not in args:
        return ("cep não existe", 400)
    if len(args["cep"]) != 8 or not args["cep"].isnumeric():
        return ("cep inválido", 400)
    with open("batata.txt", mode="a") as file:
        file.write(f"{args['cep']}\n")
        return ("cep valido", 201)


""" segunda questão """
# crie um novo endpoint que receba um cep dinamicamente no path/caminho da url e receba isso como parâmetro da função.
# após receber esses parâmetro de cep verifique se o mesmo já está no arquivo de ceps.
# caso esteja, retorne uma mensagem informando.
# mensagem: {"message":"o cep {cep} está cadastrado."}
# código de status: 200
# headers: do tipo application json
# caso não esteja, retorne uma mensagem informando que não foi encontrado e retorne 400 e o header como application json


@app.route("/cep/<cep>/")
def cep_dinamicamente(cep):
    with open("batata.txt", mode="r") as file:
        text = file.read()
        if cep in text:
            return {"message": f"o cep {cep} está cadastrado."}
        return ({"message": f"o cep {cep} não está cadastrado."}, 400)


# como retornar html ao invés de uma string ou array.


@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/for/<nome>/")
def index_for(nome):
    title = f"olá eu sou o {nome}"
    users = [
        {"username": nome, "url": "https://www.google.com"},
    ]
    return render_template("for.html", title=title, users=users)


@app.route("/if/<nome>")
def index_if(nome):
    title = "olá eu sou o {nome}"
    users = [{"username": nome}]
    return render_template("if.html", title=title, users=users)


# for i in a:
#     i['url']

# {% for i in a %}
#     {{ i.url }}
# {% endfor %}
users_list = []


@app.route("/add/user/")
def add_user():
    args = dict(request.args)
    if "username" not in args or "url" not in args:
        return ({"message": "invalid user"}, 400)

    users_list.append(args)
    return ({"message": "add user success"}, 201)


@app.route("/get/users/")
def get_user():
    return render_template("users.html", users=users_list)
