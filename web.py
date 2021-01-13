from flask import Flask
from app import MyStreamListener

app = Flask(__name__)


@app.route('/')
def homepage():
    return MyStreamListener.on_status

if __name__ == '__main__':
    app.run()