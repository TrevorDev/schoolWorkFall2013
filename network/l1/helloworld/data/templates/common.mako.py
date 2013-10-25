# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1382733138.651463
_enable_loop = True
_template_filename = u'/home/trevor/workspace/schoolWorkFall2013/network/l1/helloworld/helloworld/templates/common.mako'
_template_uri = u'/common.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['navbar', 'top', 'bottomIncludes']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\n    <div class="navbar navbar-inverse">\n      <div class="container-wide">\n        <div class="navbar-header">\n          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n\n          </button>\n          <a class="navbar-brand" href="#">Trevor Baron 0710828 Lab</a>\n        </div>\n        <!--<div class="navbar-collapse collapse">\n          <ul class="nav navbar-nav">\n            <li class="active"><a href="#">Home</a></li>\n            <li><a href="#about">About</a></li>\n\n            <li><a href="#contact">Contact</a></li>\n            <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li><a href="#">Action</a></li>\n                <li><a href="#">Another action</a></li>\n                <li><a href="#">Something else here</a></li>\n\n                <li class="divider"></li>\n                <li class="dropdown-header">Nav header</li>\n                <li><a href="#">Separated link</a></li>\n              </ul>\n            </li>\n          </ul>\n        </div>-->\n        <div class="navbar-collapse collapse">\n')
        # SOURCE LINE 51
        if request.cookies.get( 'username' ):
            # SOURCE LINE 52
            __M_writer(u'        <ul class="nav navbar-nav navbar-right">\n            <li><a href="/users/logout">Logout ')
            # SOURCE LINE 53
            __M_writer(escape(request.cookies.get( 'username' )))
            __M_writer(u'</a></li>\n        </ul>\n')
        # SOURCE LINE 56
        __M_writer(u'        </div>\n      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="">\n    <meta name="author" content="">\n    <link rel="shortcut icon" href="../../assets/ico/favicon.png">\n\n    <title>Lab</title>\n\n    <!-- Bootstrap core CSS -->\n    <link href="/bootstrap/dist/css/bootstrap.css" rel="stylesheet">\n    <link href="style.css" rel="stylesheet">\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottomIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u'\n<script src="/bootstrap/dist/js/jquery.min.js"></script>\n    <script src="/bootstrap/dist/js/bootstrap.min.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


