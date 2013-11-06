import logging, httplib

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)


class FlickrController(BaseController):

    def index(self,id):
        # Return a rendered template
        #return render('/flickr.mako')
        # or, return a string
        conn = httplib.HTTPConnection("api.flickr.com")
        conn.request("GET", "/services/rest/?method=flickr.photos.search&api_key=a6501703ec2a523726ae2b2a7d7dcdd2&tags="+id+"&per_page=20&format=json")
        resp = conn.getresponse().read()
        conn.close
        return str(resp)
