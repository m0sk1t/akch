from os import environ
from sanic import Sanic

from db.redis_client import redis_client
from db.cassandra_client import cassandra_client

from routes.posts import retrieve_post


app = Sanic()


APP_PORT = 8888
APP_HOST = '0.0.0.0'


try:
    APP_HOST = environ['APP_HOST']
    APP_PORT = environ['APP_PORT']
except KeyError as e:
    print(e.__repr__())


app.add_route(retrieve_post, '/posts/<id:int>')


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)
