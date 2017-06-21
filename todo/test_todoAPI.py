import os
import unittest

from flask import json
from todo import app

class TodoAPI_Index_TestCase(unittest.TestCase):

    # Taken from http://flask.pocoo.org/docs/0.12/testing/
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def tearDown(self):
        # Clear the todo list
        self.app.delete('/')

    def test_cors(self):
        rv = self.app.get('/', headers={"Origin": "http://www.github.com/"})
        self.assertEqual(rv.headers["Access-Control-Allow-Origin"], "http://www.github.com/")

    def test_index_get(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual([], json.loads(rv.data))

    def test_index_post(self):
        data = dict(title="Todo1")
        rv = self.app.post('/', data=json.dumps(data), content_type="application/json")
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(data["title"], json.loads(rv.data)["title"])
        self.assertEqual(None, json.loads(rv.data)["order"])
        self.assertEqual(False, json.loads(rv.data)["completed"])

    def test_index_delete(self):
        rv = self.app.delete('/')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual([], json.loads(rv.data))

    def test_index_patch(self):
        rv = self.app.patch('/')
        self.assertEqual(rv.status_code, 405)

class TodoAPI_Item_TestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.data = dict(title="Todo1")
        rv = self.app.post('/', data=json.dumps(self.data), content_type="application/json")

    def tearDown(self):
        # Clear the todo list
        self.app.delete('/')

    def test_todoURL_get(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        guid = json.loads(rv.data)[0]["url"].rsplit('/', 1)[-1]
        rv = self.app.get('/' + guid)
        self.assertEqual(self.data["title"], json.loads(rv.data)["title"])
        self.assertEqual(False, json.loads(rv.data)["completed"])

if __name__ == '__main__':
    unittest.main()
