import flask
from flask import jsonify
import sqlite3

DATABASE = './database.db'

def get_db():
    db = getattr(flask, '_database', None)
    if db is None:
        db = flask._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(flask, '_database', None)
    if db is not None:
        db.close()

@app.route("/", methods = ["GET"])
def home():
    return "Hello World"

@app.route("/stranger", methods = ["GET"])
def stranger():
    return "Hello stranger!"

@app.route("/greetings", methods = ["GET"])
def greetings():
    dict = {"spanish": "hola", "english": "hello", "french": "bonjour"}
    return jsonify(dict)

@app.route("/user", methods = ["GET"])
def index():
    users = query_db("select * from user")
    list = [user["username"] for user in users]
    print(users)
    print(list)
    return jsonify(list)

app.run()