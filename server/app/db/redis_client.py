from os import environ


from redis import Redis, ConnectionError


from constants import CM, fmtRed


try:
    REDIS_HOST = environ['REDIS_HOST']
    REDIS_PORT = environ['REDIS_PORT']
except KeyError as e:
    print(e)


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT):
        try:
            self._conn = Redis(host, port, db=0)
            print(u'%s Redis connection established: %s:%s' % (CM, host, port))
        except ConnectionError as e:
            print(e)

    def get_key(self, key=None):
        if key is None:
            return
        return self._conn.get(key)

    def set_key(self, key=None, value=None):
        if key is None:
            return
        self._conn.set(key, value)


redis_client = RedisClient()
