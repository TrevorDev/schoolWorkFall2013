# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1382731951.724825
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
        __M_writer(u'\n  </head>\n\n  <body>\n<div class="container-wide">\n<div">\n        <div id="toggle" class="col-md-3">\n        <h1>Dashboard! Welcome ')
        # SOURCE LINE 13
        __M_writer(escape(request.cookies.get( 'username' )))
        __M_writer(u'</h1>\n        <p class="lead">Greatest Image API on the web!</p>\n        </div>\n</div>\n</div> <!-- /container -->\n    <div class="navbar navbar-inverse navbar-fixed-bottom">\n      <div class="navbar-header">\n      </div>\n    </div>\n\n    <!-- Bootstrap core JavaScript\n    ================================================== -->\n    <!-- Placed at the end of the document so the pages load faster -->\n    <script src="/bootstrap/dist/js/jquery.min.js"></script>\n    <script src="/bootstrap/dist/js/bootstrap.min.js"></script>\n    <script>\n    </script>\n\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


