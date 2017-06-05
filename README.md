# Python implementation of todobackend.com
This is a (work in progress) Python implementation of the specifications of [todobackend.com](http://todobackend.com/), using [Flask](http://flask.pocoo.org/) as an web framework (with [Gunicorn](http://gunicorn.org/) as a [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) server)

## Running
To run the code locally, clone this repository, install [virtualenv](https://virtualenv.pypa.io/en/stable/) and use it to import the dependencies:
```bash
git clone https://github.com/bramfoo/todo-backend.git
cd todo-backend
pip install virtualenv
pip install -r requirements.txt
gunicorn todo:app
```
and visit [localhost:8000](http://localhost:8000/)

To run the code on a cloud server, e.g. Heroku:
(assuming you have a Heroku account and CLI set up), follow the above commands for cloning, installing virtualenv and importing dependencies, but run it using

```bash
git push heroku master
heroku open
```
## Testing
At the moment, there are no local unit tests. However, the todobackend site offers a testing suite, that can be used: visit http://todobackend.com/specs/index.html?<HEROKU_APP_NAME>, e.g. http://todobackend.com/specs/index.html?https://bramfoo-todo-backend.herokuapp.com/

## More info
This repository contains (a lot of) inspiration from [Faerbit's code](https://github.com/Faerbit/todo-backend-flask)
