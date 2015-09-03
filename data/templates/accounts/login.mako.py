# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438842250.665081
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/login.mako'
_template_uri = '/accounts/login.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../site_out.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if c.login_counter > 1:
            __M_writer(u'    Incorrect Username or Password\n')
        __M_writer(u'\n<center>\n<div class="content">\n<form action="')
        __M_writer(escape(url(controller='account', action='login_handler'
,came_from=c.came_from, __logins=c.login_counter)))
        __M_writer(u'" method="POST">\n<label for="login">username</label>\n<input type="text" id="login" name="login" /><br />\n<label for="password">password</label>\n<input type="password" id="password" name="password" /><br />\n<input type="submit" id="submit" value="Submit" />\n</form>\n</div>\n\n')
        if "join/" in c.came_from:
            __M_writer(u'\tdon\'t have an account yet? <a href="')
            __M_writer(escape(url(controller='account', action='create_account', then_join=c.came_from.split("join/")[1])))
            __M_writer(u'">register here</a>.<br/>\t\n')
        else:
            __M_writer(u'\tdon\'t have an account yet? <a href="')
            __M_writer(escape(url(controller='account', action='create_account')))
            __M_writer(u'">register here</a>.<br/>\n')
        __M_writer(u'or maybe you forget your password? <a href="')
        __M_writer(escape(url(controller='account', action='recover_password')))
        __M_writer(u'">recover it</a>.\n</center>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'home')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 2, "36": 4, "37": 5, "38": 7, "39": 10, "41": 11, "42": 20, "43": 21, "44": 21, "45": 21, "46": 22, "47": 23, "48": 23, "49": 23, "50": 25, "51": 25, "52": 25, "58": 2, "62": 2, "68": 62}, "uri": "/accounts/login.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/login.mako"}
__M_END_METADATA
"""
