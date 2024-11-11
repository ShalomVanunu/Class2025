from flask import Flask,render_template,request
import socket

app = Flask(__name__)

def send_data(code):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the server hostname and port
    host = "172.20.143.77"  # Replace with server IP if needed
    port = 5544
    # Connect to the server
    client_socket.connect((host, port))
    client_socket.send(code.encode("utf-8"))
    data_recv = client_socket.recv(1024).decode('utf-8')
    return data_recv



@app.route("/" , methods= ["POST","GET"])
def main_page():
    if request.method=="POST":
        code = request.form["cardnum"]
        data_recv = send_data(code)
        if data_recv != "No name found for this card number.":
            return f"<h1> {data_recv} </h1>"
        else:
            return render_template("index.html" , content = "Try Again")
    else:
        return render_template("index.html" , content = "")


app.run(port=80, debug=True, host="172.20.143.77")
