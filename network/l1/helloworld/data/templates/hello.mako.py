# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1378920647.310483
_enable_loop = True
_template_filename = '/home/undergrad/2/tbaron/Documents/schoolWorkFall2013/network/l1/helloworld/helloworld/templates/hello.mako'
_template_uri = '/hello.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="">\n    <meta name="author" content="">\n    <link rel="shortcut icon" href="../../assets/ico/favicon.png">\n\n    <title>Lab 1</title>\n\n    <!-- Bootstrap core CSS -->\n    <link href="/bootstrap/dist/css/bootstrap.css" rel="stylesheet">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n      <script src="../../assets/js/html5shiv.js"></script>\n      <script src="../../assets/js/respond.min.js"></script>\n    <![endif]-->\n  </head>\n\n  <body>\n\n    <div class="navbar navbar-inverse navbar-fixed-top">\n      <div class="container">\n        <div class="navbar-header">\n          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n\n          </button>\n          <a class="navbar-brand" href="#">Trevor\'s Lab</a>\n        </div>\n        <div class="navbar-collapse collapse">\n          <ul class="nav navbar-nav">\n            <li class="active"><a href="#">Home</a></li>\n            <li><a href="#about">About</a></li>\n\n            <li><a href="#contact">Contact</a></li>\n            <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li><a href="#">Action</a></li>\n                <li><a href="#">Another action</a></li>\n                <li><a href="#">Something else here</a></li>\n\n                <li class="divider"></li>\n                <li class="dropdown-header">Nav header</li>\n                <li><a href="#">Separated link</a></li>\n                <li><a href="#">One more separated link</a></li>\n              </ul>\n            </li>\n          </ul>\n        </div><!--/.navbar-collapse -->\n      </div>\n    </div>\n\n    <!-- Main jumbotron for a primary marketing message or call to action -->\n    <div class="jumbotron">\n      <div class="container">\n        <h1>Lab 1!</h1>\n\n        <p>This is my networks lab1 bootstrap page.</p>\n        <p><a id="actionButton" class="btn btn-primary btn-lg">Trigger Alert &raquo;</a></p>\n      </div>\n    </div>\n\n    <div class="container">\n      <!-- Example row of columns -->\n      <!--<div class="row">\n\n        <div class="col-lg-4">\n          <h2>Heading</h2>\n          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>\n          <p><a class="btn btn-default" href="#">View details &raquo;</a></p>\n        </div>\n        <div class="col-lg-4">\n          <h2>Heading</h2>\n\n          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>\n          <p><a class="btn btn-default" href="#">View details &raquo;</a></p>\n       </div>\n        <div class="col-lg-4">\n          <h2>Heading</h2>\n          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>\n          <p><a class="btn btn-default" href="#">View details &raquo;</a></p>\n\n        </div>\n      </div>-->\n\n      <hr>\n    </div> <!-- /container -->\n\n\n    <!-- Bootstrap core JavaScript\n    ================================================== -->\n    <!-- Placed at the end of the document so the pages load faster -->\n    <script src="/bootstrap/dist/js/jquery.min.js"></script>\n    <script src="/bootstrap/dist/js/bootstrap.min.js"></script>\n    <script>\n\t$(\'#actionButton\').click(function(){\n\t\talert(\'jquery click event triggered\');\n\t});\n    </script>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


