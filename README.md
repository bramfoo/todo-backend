# Python implementation of todobackend.com
This is a Python implementation of the specifications of [todobackend.com](http://todobackend.com/), using [Flask](http://flask.pocoo.org/) as an web framework (with [Gunicorn](http://gunicorn.org/) as a [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) server)

## Running
To run the code locally:
`gunicorn todo:app`
and visit [localhost:8000](http://localhost:8000/)

To run the code on a cloud server, e.g. Heroku:
(assuming you have a Heroku account and CLI set up)

```bash
git push heroku master
heroku open
```
