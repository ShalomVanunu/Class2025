from flask import Flask,render_template,request
import socket

app = Flask(__name__)

def send_data(code):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the server hostname and port
    host = "172.20.143.77"  # Replace with server IP if needed
    port = 5555
    # Connect to the server
    client_socket.connect((host, port))
    client_socket.send(code.encode("utf-8"))
    print(client_socket.recv(1024).decode('utf-8'))



@app.route("/" , methods= ["POST","GET"])
def main_page():
    if request.method=="POST":
        code = request.form["cardnum"]
        send_data(code)
        return render_template("index.html")
    else:
        return render_template("index.html")


app.run(port=80, debug=True, host="172.20.143.77")
