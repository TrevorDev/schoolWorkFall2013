import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

class DashboardController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/dashboard.mako')
        # or, return a string
        if request.cookies.get( 'username' ):
        	c.test='cool';
        	return render('/dashboard.mako')
        else:
        	return redirect(url('/')) 


