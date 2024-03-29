# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1382733580.172409
_enable_loop = True
_template_filename = '/home/trevor/workspace/schoolWorkFall2013/network/l1/helloworld/helloworld/templates/index.mako'
_template_uri = '/index.mako'
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
        common = _mako_get_namespace(context, 'common')
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n')
        # SOURCE LINE 5
        __M_writer(escape(common.top()))
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(common.navbar()))
        __M_writer(u'\n  </head>\n\n  <body>\n<div class="container-wide">\n<div class="jumbotron" style="background-color: transparent;">\n        <div class="col-md-3">\n        <h1>Boost Pic</h1>\n        <p class="lead">Greatest Image API on the web!</p>\n        </div>\n        <div class="col-md-6">\n          <div id="alert" style="display: none;" class="alert alert-warning"></div>\n          <h1>Sign In</h1>\n          <div class="input-group input-group-lg" style="padding-bottom:5px">\n            <span class="input-group-addon"><span class="glyphicon glyphicon-user"></span></span>\n            <input id="user" type="text" class="form-control" placeholder="Username">\n          </div>\n          <div class="input-group input-group-lg">\n          <span class="input-group-addon"><span class="glyphicon glyphicon-lock"></span></span>\n            <input id="pass" type="password" class="form-control" placeholder="Password">\n            </div>\n        <p style="text-align:right;margin-top:5px;"><a style="margin-bottom:5px;" id="signIn" class="btn btn-lg btn-success" href="#">Sign In <span class="glyphicon glyphicon-circle-arrow-right"></span></a><br><a id="signUp" class="btn btn-lg btn-success" href="#">Don\'t have an account? Please sign up <span class="glyphicon glyphicon-circle-arrow-right"></span></a></p>\n\n        <div id="toggle" style="text-align:right;margin-top:5px;display: none;" class="panel panel-primary">\n          <div class="panel-heading">\n          <h3 class="panel-title">Sign up</h3>\n        </div>\n          <div style="padding:30px">\n          <div class="input-group input-group-lg" style="padding-bottom:5px">\n            <span class="input-group-addon"><span class="glyphicon glyphicon-user"></span></span>\n            <input id="signupUser" type="text" class="form-control" placeholder="Username">\n          </div>\n          <div class="input-group input-group-lg" style="padding-bottom:5px">\n            <span class="input-group-addon"><span class="glyphicon glyphicon-lock"></span></span>\n            <input id="signupPass" type="password" class="form-control" placeholder="Password">\n          </div>\n          <div class="input-group input-group-lg" style="padding-bottom:5px">\n            <span class="input-group-addon"><span class="glyphicon glyphicon-lock"></span></span>\n            <input id="repeatPass" type="password" class="form-control" placeholder="Repeat Password">\n          </div>\n          <a style="margin-bottom:5px;" id="create" class="btn btn-lg btn-success" href="#">Create <span class="glyphicon glyphicon-circle-arrow-right"></span></a>\n        </div>\n        </div>\n        </div>\n        <div class="col-md-3">\n        <img style="width:300px;" id="banana" src="/camera_icon.svg">\n        </div>\n</div>\n</div> <!-- /container -->\n    <div class="navbar navbar-inverse navbar-fixed-bottom" style="z-index:-1;">\n      <div class="navbar-header">\n          <p class="navbar-brand">\n            Login with usernmae:testUser password:test<br>\n            observe that dashboard page loads and displays username<br>\n            attempt to go to 127.0.0.1:5000 again and see that you get redirected to dash<br>\n            click logout<br>\n            attempt to got to 127.0.0.1:5000/dashboard<br>\n            observe that you get redirected to login/create account page\n          </p>\n          \n      </div>\n    </div>\n    ')
        # SOURCE LINE 68
        __M_writer(escape(common.bottomIncludes()))
        __M_writer(u'\n    <script>\n    var attempt = 0;\n    $("#signIn").click(function(event){\n      $.ajax({\n        url: "/users/auth",\n        method: "post",\n        data: { username: $("#user").val(), password: $("#pass").val() },\n        context: document.body\n      }).done(function(data) {\n          if(data==\'success\'){\n            window.location.href = "/dashboard";\n          }else{\n            attempt++;\n            $("#alert").html(\'<strong>Warning!</strong> Invalid Login Info. \'+attempt+\' Attempts\');\n            $("#alert").css("display", "block");\n          }\n      });\n        \n    });\n\n    $("#create").click(function(event){\n        if($("#repeatPass").val()!=$("#signupPass").val()){\n          $("#alert").html(\'<strong>Warning!</strong> Passwords do not match\');\n          $("#alert").css("display", "block");\n        }else{\n          $.ajax({\n            url: "/users",\n            method: "put",\n            data: { username: $("#signupUser").val(), password: $("#repeatPass").val() },\n            context: document.body\n          }).done(function(data) {\n            $("#alert").html(\'<strong>Account Created!</strong>\');\n            $("#alert").css("display", "block");\n          });\n        }\n    });\n    $("#signUp").click(function(event){\n        //window.location.href = "/signup";\n        $("#toggle").slideToggle( "slow", function() {\n        });\n    });\n    </script>\n\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


