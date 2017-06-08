from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

import todo.todoAPI
