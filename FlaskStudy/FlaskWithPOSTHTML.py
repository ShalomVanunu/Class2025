from Tools.scripts.make_ctype import method
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/" , methods= ["POST","GET"])
def main_page():
    if request.method=="POST":
        code = request.form["code"]
        password = request.form["password"]
        print(code,password)
        return render_template("index.html")
    else:
        return render_template("login-form.html")

@app.route("/success")
def success():
    return "<h1> Success </h1>"



app.run(port=80, debug=True, host="172.20.143.77")
