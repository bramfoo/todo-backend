import sys
import uuid
import logging

from flask import jsonify, request, url_for

from todo import app
from todo.item import Item


todos = {}
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        response = []
        for key in todos.keys():
            response.append(toDict(key))
        logging.debug("GET: " + str(response))
        return jsonify(response)

    if request.method == 'POST':
        req_data = request.get_json()
        logging.debug("POST data: " + str(req_data))

        todo_uuid = uuid.uuid4()
        todo = Item(req_data["title"])
        logging.debug("Created todo: " + str(todo))

        todos[todo_uuid] = todo
        return jsonify(toDict(todo_uuid))

    if request.method == 'DELETE':
        logging.debug("DELETE: " + str(request))
        # Returning empty response
        return ('', 204)
    else:
        logging.debug(request.method + str(request))
        return ('', 204)

@app.route('/<uuid:todo_uuid>', methods=["GET"])
def todo(todo_uuid):
    logging.debug("/<uuid>: " + str(request.path))
    if request.method == 'GET':
        if todo_uuid in todos:
            return jsonify(toDict(todo_uuid))
        else:
            logging.debug("Item not found")
            return jsonify(dict())
    else:
        return ('', 204)

def toDict(key):
    # Build URL based on the 'item' function
    # See http://flask.pocoo.org/docs/0.12/quickstart/#url-building
    item = todos[key]
    return dict(title=item.title, completed=item.completed, url=url_for("todo", todo_uuid=key, _external=True))
