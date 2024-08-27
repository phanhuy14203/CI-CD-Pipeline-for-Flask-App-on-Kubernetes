from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    container_name = os.getenv("HOSTNAME")
    return f'Hello from pod: {container_name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
