from flask import Flask, request
import socket 
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    global seed
    if request.method == 'POST':
        subprocess.Popen(['python3', '-u', 'stress_cpu.py'])
    else:
        return f"{socket.gethostname()}"


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80)
