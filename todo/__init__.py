from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def todo():
    if request.method == 'GET':
        return "GET of root URL"
    if request.method == 'POST':
        return request.data
    if request.method == 'DELETE':
        return "DELETE on root URL"
    else:
        return "Method on root URL " + str(request.method)

if __name__ == "__main__":
    app.run()