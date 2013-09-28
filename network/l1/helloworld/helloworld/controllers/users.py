import logging
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

allUsers = {0: "Trevor", 1: "Jack"}
idCounter = 2
class UsersController(BaseController):

    def index(self, id):
        global allUsers
        global idCounter
        c.users=allUsers
        try:
            if request.method=="GET":
                return json.dumps({int(id): c.users[int(id)]});
            elif request.method=="PUT":
                allUsers[idCounter] = id
                idCounter=idCounter+1
                c.users=allUsers
                return json.dumps(c.users)
            elif request.method=="DELETE":
                del allUsers[int(id)]
                c.users=allUsers
                return json.dumps(c.users)
            else:
                return {"success": False}
        except:
            return {"success": False}
    def all(self):    
        global allUsers
        c.users=allUsers
        try:
            if request.method=="GET":
                return json.dumps(c.users)
            else:
                return {"success": False}
        except:
            return {"success": False}
    def edit(self,id,name):    
        global allUsers
        try:
            if request.method=="POST" and allUsers[int(id)]:
                allUsers[int(id)]=name
                c.users=allUsers
                return json.dumps(c.users[int(id)])
            else:
                return {"success": False}
        except:
            return {"success": False}