import sys
import uuid
import logging

from flask import jsonify, request, url_for

from todo import app
from todo.item import Item


todos = {}
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def todo():
    if request.method == 'GET':
        response = []
        for key in todos.keys():
            response.append(toDict(key))
        logging.debug("GET: " + str(response))
        return jsonify(response)

    if request.method == 'POST':
        req_data = request.get_json()
        logging.debug("POST data: " + str(req_data))

        todoUID = uuid.uuid4().hex
        todo = Item(req_data["title"])
        logging.debug("Created todo: " + str(todo))

        todos[todoUID] = todo
        return jsonify(toDict(todoUID))

    if request.method == 'DELETE':
        logging.debug("DELETE: " + str(request))
        return
    else:
        logging.debug(request.method + str(request))
        return

@app.route("/<uuid:item_id>", methods=["GET"])
def item(item_id):
    if todos[item_id]:
        return jsonify(toDict(item_id))
    else:
        return jsonify(dict())

def toDict(key):
    # Build URL based on the 'item' function
    # See http://flask.pocoo.org/docs/0.12/quickstart/#url-building
    item = todos[key]
    return dict(title=item.title, completed=item.completed, url=url_for("item", item_id=key, _external=True))
