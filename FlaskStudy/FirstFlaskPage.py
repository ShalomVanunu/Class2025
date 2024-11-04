
from flask import Flask


app = Flask(__name__)

@app.route("/") # main page
def Home():
    return '<h1> Wellcome Class</h1>'

@app.route("/sport") # sport page
def Sport():
    return '<h1> Wellcome SportPage</h1>'

@app.route("/<NAME>") # sport page
def Show_Name(NAME):
    return f"<h2> My Name {NAME} </h2> "


app.run(port=80, debug=True, host="172.20.143.77")


