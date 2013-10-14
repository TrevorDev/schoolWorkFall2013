from helloworld.tests import *

class TestUsersController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='users', action='index'))
        # Test response...
        assert 'Jack' in response
        assert 'Trevor' in response

    def test_get(self):
        response = self.app.get(url(controller='users', action='index', id=1))
        # Test response...
        assert ('Jack' in response)
        assert ('Trevor' not in response)

    def test_delete(self):
        response = self.app.delete(url(controller='users', action='index', id=0))
        response = self.app.get(url(controller='users', action='index'))
        # Test response...
        assert ('Jack' in response)
        assert ('Trevor' not in response)
        response = self.app.put(url(controller='users', action='index', id='Trevor'))

    def test_put(self):
        response = self.app.put(url(controller='users', action='index', id='Bob'))
        response = self.app.get(url(controller='users', action='index'))
        assert ('Bob' in response)

    def test_post(self):
        response = self.app.post(url(controller='users', action='index', id='1', name="Emily"))
        response = self.app.get(url(controller='users', action='index'))
        assert ('Emily' in response)
