from os import environ


from cassandra.cluster import Cluster


from constants import CM, CR, fmtRed


try:
    CASSANDRA_HOST = environ['CASSANDRA_HOST']
except KeyError as e:
    print(e)


class CassandraClient(object):
    def __init__(self, host=CASSANDRA_HOST):
        try:
            cluster = Cluster([host])
            self._session = cluster.connect()
            print(u'%s Cassandra connection established: %s:9042' % (CM, host))
        except BaseException as e:
            print(fmtRed('✞ Cassandra connection error: %s' % (e,)))

    def retrieve_post(self, post_id=None):
        if post_id is None:
            return
        post = self._session \
            .execute('SELECT * FROM posts WHERE id=%' % (post_id,))
        print(post_by_id)


cassandra_client = CassandraClient()
