# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1383348710.066017
_enable_loop = True
_template_filename = '/home/trevor/workspace/schoolWorkFall2013/network/l1/helloworld/helloworld/templates/dashboard.mako'
_template_uri = '/dashboard.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace(u'common', context._clean_inheritance_tokens(), templateuri=u'common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'common')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        common = _mako_get_namespace(context, 'common')
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n')
        # SOURCE LINE 5
        __M_writer(escape(common.top()))
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(common.navbar()))
        __M_writer(u'\n  </head>\n\n  <body>\n<div class="container-wide">\n<div>\n        <div id="toggle" class="col-md-3">\n        <h1>Dashboard! Welcome ')
        # SOURCE LINE 13
        __M_writer(escape(request.cookies.get( 'username' )))
        __M_writer(u'</h1>\n        <p class="lead">Greatest Image API on the web!</p>\n        <input class="form-control" id="searchWord" placeholder="Enter image keyword"><br>\n        <a id="search" class="btn btn-lg btn-success">Search</a>\n        <img style="width:300px;visibility:hidden;" id="loading" src="/loading-gif.gif">\n        </div>\n        <div id="toggle" class="col-md-9">\n        \n        <div id="imgsBox">\n        </div>\n        </div>\n</div>\n</div> <!-- /container -->\n    <div class="navbar navbar-inverse navbar-fixed-bottom">\n      <div class="navbar-header">\n      </div>\n    </div>\n\n    <!-- Bootstrap core JavaScript\n    ================================================== -->\n    <!-- Placed at the end of the document so the pages load faster -->\n    <script src="/bootstrap/dist/js/jquery.min.js"></script>\n    <script src="/bootstrap/dist/js/bootstrap.min.js"></script>\n    <script>\n    </script>\n\n  </body>\n\n\n\n  <script>\n    /*var attempt = 0;\n    function jsonFlickrApi(rsp) {\n        var s = "";\n        // http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg\n        // http://www.flickr.com/photos/{user-id}/{photo-id}\n        s = "Results: " + rsp.photos.photo.length + "<br/>";\n        \n        for (var i=0; i < rsp.photos.photo.length; i++) {\n          photo = rsp.photos.photo[i];\n          t_url = "http://farm" + photo.farm + ".static.flickr.com/" + \n            photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";\n          p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;\n          s +=  \'<a href="\' + p_url + \'">\' + \'<img alt="\'+ photo.title + \n            \'"src="\' + t_url + \'"/>\' + \'</a>\';\n        }\n        console.log(s);\n         $("#imgsBox").html(s);\n        \n    }\n    $("#search").click(function(event){\n      $.ajax({\n        dataType: "jsonp",\n        url: "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=a6501703ec2a523726ae2b2a7d7dcdd2&tags="+$("#searchWord").val()+"&per_page=15&format=json",\n        method: "get"\n      });\n        \n    });*/\n\n      function jsonFlickrApi(rsp) {\n      $("#loading").css("visibility","hidden");\n        var s = "";\n        // http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg\n        // http://www.flickr.com/photos/{user-id}/{photo-id}\n        s = "total number is: " + rsp.photos.photo.length + "<br/>";\n        \n        for (var i=0; i < rsp.photos.photo.length; i++) {\n          photo = rsp.photos.photo[i];\n          t_url = "http://farm" + photo.farm + ".static.flickr.com/" + \n            photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";\n          p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;\n          s +=  \'<a href="\' + p_url + \'">\' + \'<img alt="\'+ photo.title + \n            \'"src="\' + t_url + \'"/>\' + \'</a>\';\n        }\n         $("#imgsBox").html(s);\n        \n    }\n\n     $("#search").click(function(event){\n     if($("#searchWord").val().length>0){\n     $("#loading").css("visibility","visible");\n      $.ajax({\n        dataType: "jsonp",\n        url: "/flickr/index/"+$("#searchWord").val(),\n        method: "get"\n      })\n        }\n    });\n    </script>\n\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


