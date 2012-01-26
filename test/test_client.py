import kosmonaut
import unittest
import os

class TestKosmonautClient(unittest.TestCase):

    def setUp(self):
        token = os.environ['VHOST_TOKEN']
        self.c = kosmonaut.Client('wr://%s@127.0.0.1:8081/test' % token)
        self.assertIsNotNone(self.c)

    def test_api(self):
        self._test_open_channel()
        #self._test_open_channel_with_invalid_name()
        #self._test_broadcast()
        #self._test_broadcast_to_not_existing_channel()
        #self._test_close_channel()
        #self._test_close_not_existing_channel()
        #self._test_request_single_access_token()

    def _test_open_channel(self):
        self.c.open_channel('foo')
