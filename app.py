from flask import Flask, request
app = Flask(__name__)
seed = 0

@app.route('/', methods=['POST', 'GET'])
def index():
    global seed
    if request.method == 'POST':
        data = request.get_json()
        seed = data.get('num', '')
    
    return f"{seed}"


if __name__ == '__main__':
   app.run()