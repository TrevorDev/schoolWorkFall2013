import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

allUsers = {0: "Trevor", 1: "Jack"}

class UsersController(BaseController):

    def index(self):
    	global allUsers
        c.users=allUsers;
        return render('/users.mako')
