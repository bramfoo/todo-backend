from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return "GET of root URL"
    else:
        return "POST to root URL"

if __name__ == "__main__":
    app.run()
