from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/directory">디렉토리로 이동</a>'

app.run(host='127.0.0.1', debug=True)