# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1379353752.426333
_enable_loop = True
_template_filename = '/home/undergrad/2/tbaron/Documents/schoolWorkFall2013/network/l1/helloworld/helloworld/templates/restTest.mako'
_template_uri = '/restTest.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<title>Test #3</title>\n</head>\n<body>\n<p>Hello numbers ')
        # SOURCE LINE 6
        __M_writer(escape(c.id))
        __M_writer(u'.</p>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


