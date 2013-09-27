import logging
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

allUsers = {0: "Trevor", 1: "Jack"}
idCounter = 2;
class UsersController(BaseController):

    def index(self, id):
        global allUsers
        global idCounter
        c.users=allUsers;
        if request.method=="GET":
            return json.dumps(c.users[int(id)]);
        elif request.method=="PUT":
            allUsers[idCounter] = id
            idCounter=idCounter+1
            c.users=allUsers;
            return json.dumps(c.users);
        elif request.method=="POST":
            return json.dumps(c.users[int(id)]);
        elif request.method=="DELETE":
            del allUsers[int(id)]
            c.users=allUsers;
            return json.dumps(c.users);
        else:
            return "Error";
    def all(self):    
        global allUsers
        c.users=allUsers;
        if request.method=="GET":
            return json.dumps(c.users);
        else:
            return "Error";