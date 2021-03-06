# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438822370.824367
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/account.mako'
_template_uri = '/accounts/account.mako'
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
    return runtime._inherit_from(context, u'../site.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<script type=\'text/javascript\'>\n\n\t$(document).ready( function() {\n\n\t    $( "#citation-settings-help" ).dialog({\n\t        height: 200,\n\t        width:300, \n\t        modal: false,\n\t        autoOpen: false,\n\t        show: "blind",\n\t    });\n\n\t    jQuery("#citation-settings-help-link").click(function(){\n\t        $("#citation-settings-help" ).dialog( "open" );\n\t    });\n\t\n\t});\n\n</script>\n\n\n<div class="content">\n\t<h3>')
        __M_writer(escape(c.account_msg))
        __M_writer(u'</h3>\n\t<center>\n\t\t<table class="form_table">\n\t\t\t')
        __M_writer(escape(h.form(url(controller='account', action='change_password'))))
        __M_writer(u'\n\t\t\t\t<tr><td><h3>Password Change:</h3></td><td></td></tr>\n\t\t\t\t<tr><td><label>new password:</td> <td>')
        __M_writer(escape(h.text('password', type='password')))
        __M_writer(u'</label></td></tr>\n\t\t\t\t<tr><td><label>confirm new password:</td> <td>')
        __M_writer(escape(h.text('password_confirm', type='password')))
        __M_writer(u'</label></td></tr>\n\t\t\t\t<tr><td></td><td>')
        __M_writer(escape(h.submit('post', 'change password')))
        __M_writer(u'</td></tr>\n\t\t\t')
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\t\t</table>\n\t</center>\n</div>\n\n\n<div class="content">\n\t<h3>')
        __M_writer(escape(c.account_msg_citation_settings))
        __M_writer(u'</h3>\n\t<center>\n\t\t<table class="form_table">\n\t\t\t')
        __M_writer(escape(h.form(url(controller='account', action='customize_citations'))))
        __M_writer(u'\n\n\t\t\t\t<tr><td><h3>Citation Settings (<a href="#" id="citation-settings-help-link">need help?</a>):</h3></td><td></td></tr>\n\t\t\t\t<tr>\n\t\t\t\t\t<td><label>Journal:</td>\n\t\t\t\t\t<td>')
        __M_writer(escape(h.select("toggle_journal", None, ["Show", "Hide"])))
        __M_writer(u' </label></td>\n\t\t\t\t</tr>\n\t\t\t\t<tr>\n\t\t\t\t\t<td><label>Authors:</td>\n\t\t\t\t\t<td>')
        __M_writer(escape(h.select("toggle_authors", None, ["Show", "Hide"])))
        __M_writer(u' </label></td>\n\t\t\t\t</tr>\n\t\t\t\t<tr>\n\t\t\t\t\t<td><label>Keywords:</td>\n\t\t\t\t\t<td>')
        __M_writer(escape(h.select("toggle_keywords", None, ["Show", "Hide"])))
        __M_writer(u' </label></td>\n\t\t\t\t</tr>\n\n\t\t\t\t<tr><td></td><td>')
        __M_writer(escape(h.submit('post', 'Apply Settings')))
        __M_writer(u'</td></tr>\n\n\t\t\t')
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\t\t</table>\n\t</center>\n</div>\n\n\n<div id="citation-settings-help" class="ui-dialog">\n    <p>The <b>Citation Settings</b> section gives you the option to customize the content of the abstracts you will see during screening.</p>\n    <p>You have the option to <i>show</i> or <i>hide</i> the <b>title</b> of the paper, the name of the <b>journal</b>, the <b>authors</b> of the paper, and/or the <b>keywords</b> associated with the abstract.</p>\n    <p>Just make your selections and click on \'Apply Settings\'.</p>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'my account')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 3, "37": 27, "38": 27, "39": 30, "40": 30, "41": 32, "42": 32, "43": 33, "44": 33, "45": 34, "46": 34, "47": 35, "48": 35, "49": 42, "50": 42, "51": 45, "52": 45, "53": 50, "54": 50, "55": 54, "56": 54, "57": 58, "58": 58, "59": 61, "60": 61, "61": 63, "62": 63, "68": 3, "72": 3, "78": 72}, "uri": "/accounts/account.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/account.mako"}
__M_END_METADATA
"""
