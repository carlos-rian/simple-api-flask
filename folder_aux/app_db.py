from flask import Flask, Response
from db.test.db_array import get_value, add_value, get_next_id, remove_value, update_value, get_all_values
from json import dumps

app = Flask(__name__)


@app.route("/get/<int:id>/")
def get(id):
    data = get_value(id=id)
    return Response(dumps(data), status=200, headers={"Content-type": "application/json"})


@app.route("/get/")
def get_all():
    data = get_all_values()
    return Response(dumps(data), status=200, headers={"Content-type": "application/json"})


@app.route("/add/")
def add():
    value = {"nome": "carlos", "idade": 26, "altura": 1.77, "solteiro": False}
    id = get_next_id()
    message = add_value(id=id, value=value)
    return Response(response=message, status=201, headers={"Content-type": "application/json"})


@app.route("/remove/<int:id>/")
def remove(id):
    data = remove_value(id=id)
    return Response(response=data, status=200, headers={"Content-type": "application/json"})


@app.route("/update/<int:id>/")
def update(id):
    value = {"nome": "Thais", "idade": 26, "altura": 1.69, "solteiro": False}
    data = update_value(id=id, value=value)
    return Response(response=data, status=200, headers={"Content-type": "application/json"})


app.run(debug=True)
