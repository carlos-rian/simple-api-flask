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


users_list = []


@app.route("/add/user/", methods=["POST"])
def add_user():
    args = dict(request.args)
    if "username" not in args or "url" not in args:
        return ({"message": "invalid user"}, 400)

    users_list.append(args)
    return ({"message": "add user success"}, 201)


@app.route("/get/users/")
def get_user():
    return render_template("users.html", users=users_list)


@app.route("/file/", methods=["GET", "POST"])
def files():
    if request.method == "GET":
        return render_template("form.html")

    files = request.files.getlist("file")

    for file in files:
        path = f"app/file/{file.filename}"
        file.save(path)

    return ({"message": "Olá esse method é um post"}, 201)


# criar banco de dados em memoria

banco_de_dados = []


@app.route("/pessoa/", methods=["GET"])
@app.route("/pessoa/<int:id>/", methods=["GET"])
def get_pessoa(id: int = None) -> dict:
    """ 
    consultar um id e retornar um dict caso exista, 
    caso não ele retornar vazio e status 400 
    """
    if not id:
        return {"pessoas": banco_de_dados}

    for pessoa in banco_de_dados:
        if id in pessoa:
            return (pessoa, 200)
    return ({"message": "id não encontrado"}, 400)


@app.route("/pessoa/", methods=["POST"])
def add_pessoa():
    """ criar um registro, caso o body não seja vazio."""
    dados = request.json
    condition = ("nome" in dados, "idade" in dados, "altura" in dados, "cor_de_pele" in dados)
    if not all(condition):
        return ({"message": "dados invalidos"}, 400)

    aux = 0
    for i in banco_de_dados:
        pivot = list(i.keys())[0]
        if aux < pivot:
            aux = pivot
    id = aux + 1
    banco_de_dados.append({id: dados})
    return ({"message": f"usuário {dados['nome']} inserido com sucesso."}, 200)


@app.route("/pessoa/<int:id>/", methods=["DELETE"])
def delete_pessoa(id: int):
    aux = None
    for index, value in enumerate(banco_de_dados):
        if id in value:
            aux = index

    if aux is not None:
        result = banco_de_dados.pop(aux)
        return ({"message": "usuário removido com sucesso", "user": result}, 200)

    return ({"message": "usuário não encontrad"}, 404)


@app.route("/pessoa/<int:id>/", methods=["PUT"])
def update_pessoa(id: int):
    dados = request.json
    condition = ("nome" in dados, "idade" in dados, "altura" in dados, "cor_de_pele" in dados)
    if not all(condition):
        return ({"message": "dados invalidos"}, 400)

    for index, value in enumerate(banco_de_dados):
        if id in value:
            banco_de_dados[index].update({id: dados})
            return ({"message": "dados atualizados"}, 200)
    return ({"message": "dados invalidos"}, 400)
