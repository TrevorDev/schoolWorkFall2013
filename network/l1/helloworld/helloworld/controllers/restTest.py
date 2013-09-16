import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ResttestController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/restTest.mako')
        # or, return a string
        return render('/restTest.mako')
    def test(self, id):
        # Return a rendered template
        #return render('/restTest.mako')
        # or, return a string
        c.id=id
        return render('/restTest.mako')
