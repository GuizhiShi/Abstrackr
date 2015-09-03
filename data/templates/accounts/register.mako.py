# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438842260.81398
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/register.mako'
_template_uri = '/accounts/register.mako'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        dir = context.get('dir', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n\n<div class="content">\n    <center>\n    \n<table class="form_table">\n  \n\n ')
        __M_writer(escape(h.form(url(controller='account', action='create_account_handler', then_join=c.then_join if 'then_join' in dir(c) else ''))))
        __M_writer(u'\n    <tr><td><label>first name:</td> <td>')
        __M_writer(escape(h.text('first_name')))
        __M_writer(u'</label></td></tr>\n    <tr><td><label>last name:</td> <td>')
        __M_writer(escape(h.text('last_name')))
        __M_writer(u'</label></td></tr>\n    <tr><td><label>how many SRs have you participated in?:</td> <td>')
        __M_writer(escape(h.text('experience', size=2)))
        __M_writer(u'</label></td></tr>\n    <tr><td><label>email:</td> <td>')
        __M_writer(escape(h.text('email')))
        __M_writer(u'</label></td></tr>\n    <tr><td><label>username:</td> <td>')
        __M_writer(escape(h.text('username')))
        __M_writer(u'</label></td></tr>\n    <tr><td><label>password:</td> <td>')
        __M_writer(escape(h.text('password', type='password')))
        __M_writer(u'</label></td></tr>\n    <tr><td></td><td>')
        __M_writer(escape(h.submit('post', 'sign me up!')))
        __M_writer(u'</td></tr>\n  ')
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n  </table>\n  </center>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'register')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 11, "39": 11, "40": 12, "41": 12, "42": 13, "43": 13, "44": 14, "45": 14, "46": 15, "47": 15, "48": 16, "49": 16, "50": 17, "51": 17, "52": 18, "53": 18, "54": 19, "55": 19, "61": 2, "65": 2, "71": 65}, "uri": "/accounts/register.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/register.mako"}
__M_END_METADATA
"""
