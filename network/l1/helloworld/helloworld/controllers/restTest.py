import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)
master = 0
class ResttestController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/restTest.mako')
        # or, return a string
        return render('/restTest.mako')


    def get(self):
        global master
        c.id=master
        return render('/restTest.mako')

    def post(self):
        global master
        master=int(id)+master
        c.id=id in request.params
        return render('/restTest.mako')

    def put(self, id):
        global master
        master=int(id)
        c.id=master
        return render('/restTest.mako')

    def delete(self):
        global master
        master=0
        c.id=master
        return render('/restTest.mako')
