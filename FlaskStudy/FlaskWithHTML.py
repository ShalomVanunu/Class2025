from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

app.run(port=80, debug=True, host="172.20.143.77")
