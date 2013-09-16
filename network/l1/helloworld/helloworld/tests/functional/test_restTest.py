from helloworld.tests import *

class TestResttestController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='restTest', action='index'))
        # Test response...
