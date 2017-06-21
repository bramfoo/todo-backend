import sys
import uuid
import logging

from flask import jsonify, request, url_for

from todo import app
from todo.item import Item


todos = {}
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    logging.debug(str(request.method) + " on " + str(request.path))
    if request.method == 'GET':
        response = returnAll()
        logging.debug(response)
        return jsonify(response)

    if request.method == 'POST':
        req_data = request.get_json()
        logging.debug("POST data: " + str(req_data))

        todo_uuid = uuid.uuid4()
        if "order" in req_data:
            todo = Item(req_data["title"], req_data["order"])
        else:
            todo = Item(req_data["title"])
        logging.debug("Created todo: " + str(todo))

        todos[todo_uuid] = todo
        return jsonify(toDict(todo_uuid))

    if request.method == 'DELETE':
        todos.clear()
        return jsonify(returnAll())
    else:
        logging.debug(request.method + str(request))
        # Returning empty response
        return ('', 204)

@app.route('/<uuid:todo_uuid>', methods=["GET", "PATCH", "DELETE"])
def todo(todo_uuid):
    logging.debug(str(request.method) + " on " + str(request.path))
    if todo_uuid in todos:
        logging.debug("Found: " + str(todos[todo_uuid]))
        if request.method == 'PATCH':
            req_data = request.get_json()
            logging.debug("New data: " + str(req_data))
            todos[todo_uuid].__dict__.update(req_data.items())
            logging.debug("Updated: " + str(todos[todo_uuid]))
            return jsonify(toDict(todo_uuid))
        if request.method == 'DELETE':
            logging.debug("Removing: " + str(todos[todo_uuid]))
            del todos[todo_uuid]
            return ('', 204)
        if request.method == 'GET':
            return jsonify(toDict(todo_uuid))
        else:
            return ('', 204)
    else:
        logging.debug("Item not found")
        return jsonify(dict())

def toDict(key):
    # Build URL based on the 'item' function
    # See http://flask.pocoo.org/docs/0.12/quickstart/#url-building
    item = todos[key]
    return dict(title=item.title, order=item.order, completed=item.completed, url=url_for("todo", todo_uuid=key, _external=True))

def returnAll():
    response = []
    for key in todos.keys():
        response.append(toDict(key))
    return response
