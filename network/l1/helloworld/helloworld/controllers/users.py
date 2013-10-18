import logging
import json
import MySQLdb

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

allUsers = {0: "Trevor", 1: "Jack"}
idCounter = 2

conn = MySQLdb.connect (host = "dursley.socs.uoguelph.ca",
    user = "tbaron",
    passwd = "0710828",
    db = "cis3210")
cursor = conn.cursor()

class UsersController(BaseController):
    def auth(self):
        try:
            cursor.execute("select password from users where username = %s;",(request.params['username']))
            conn.commit()
            result=cursor.fetchone()
            if result[0] == request.params['password']:
                return {"success": True}
            else:
                return {"error": True}
        except:
            return {"error": True}
    def index(self, id=None,name=None):
        global allUsers
        global idCounter
        c.users=allUsers
        try:
            if request.method=="GET":

                #cursor.execute("INSERT INTO users (username,password) VALUES ('trevors', 'bar');")
                #conn.commit()
                if id is None:
                    cursor.execute("select * from users;")
                    conn.commit()
                    return json.dumps(cursor.fetchall())
                else:
                    cursor.execute("select * from users where userid = %s;",id)
                    conn.commit()
                    return json.dumps(cursor.fetchone());
            elif request.method=="PUT":
                cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s);", (request.params['username'],request.params['password']) )
                conn.commit()
                return {"success": True}
            elif request.method=="DELETE":
                cursor.execute("Delete from users where userid = %s;",id)
                conn.commit()
                result=cursor.fetchone()
                return {"success": True}
            elif request.method=="POST":
                cursor.execute("UPDATE users SET password=%s WHERE username=%s;",(request.params['password'],request.params['username']));
                conn.commit()
                return {"success": True}   
            else:
                return {"error": True}
        except:
            return {"error": True}