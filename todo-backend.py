from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

@app.route("/")
def hello():
    return "Poep World!"

if __name__ == "__main__":
    app.run()
