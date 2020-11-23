import os
import unittest

from flaskapp import app
from redis import Redis

class CounterTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    # define tests

    # test1
    def test_welcome_page(self):
        # make a get request, on endpoint '/'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # test2
    def test_redis_connection(self):
        redis = Redis(host="redis-server", db=0)
        self.app.get('/visit')
        self.assertEqual(int(redis.get("counter")),1)

if __name__ == "__main__":
    unittest.main()