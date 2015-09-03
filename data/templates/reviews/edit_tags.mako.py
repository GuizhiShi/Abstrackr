# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634980.978901
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/edit_tags.mako'
_template_uri = '/reviews/edit_tags.mako'
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
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        dir = context.get('dir', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n\n<script type="text/javascript">    \n\n$(document).ready(function() {\n    $( "#dialog" ).dialog({\n      height: 120,\n      modal: true,\n      autoOpen: false,\n      show: "blind",\n    });\n\n\n')
        for tag in c.tags:
            __M_writer(u'      $("#edit_button_')
            __M_writer(escape(tag.id))
            __M_writer(u'").click(function()\n      {\n\n         $("#dialog").load(\'/review/edit_tag/')
            __M_writer(escape(tag.id))
            __M_writer(u'/')
            __M_writer(escape(c.assignment_id))
            __M_writer(u'\',\n           function(){\n                $("#dialog").dialog("open");\n           });\n      });\n')
        __M_writer(u'\n    $("#close_btn").click(function (e)\n    {\n       $("#dialog" ).dialog( "close" );\n    });\n});\n\n</script>\n          \n  \n\n\n<div id="dialog"></div>\n\n')
        if "assignment_id" in dir(c):
            __M_writer(u'  <div class = "actions">\n      <a href="')
            __M_writer(escape(url(controller='review', action='screen', review_id=c.review_id, assignment_id=c.assignment_id)))
            __M_writer(u'">ok, get back to screening <img src="../../../arrow_right.png"></img></a>\n      </div>\n')
        __M_writer(u'\n<div class="content">\n\n')
        if len(c.tags) > 0:
            __M_writer(u'    your tags: <br/><br/>\n    <table class="list_table">\n        <th>tag</th>\n        <th>edit</th>\n        <th>delete</th>\n')
            for i,tag in enumerate(c.tags):
                __M_writer(u'            <tr class="')
                __M_writer(escape('odd' if i%2 else 'even'))
                __M_writer(u'">\n              <td>')
                __M_writer(escape(tag.text))
                __M_writer(u'</td>           \n              <td class="actions" align="left"><input type="button" id="edit_button_')
                __M_writer(escape(tag.id))
                __M_writer(u'" value="re-name tag..."/></td>\n                <td><a href="/review/delete_tag/')
                __M_writer(escape(tag.id))
                __M_writer(u'/')
                __M_writer(escape(c.assignment_id))
                __M_writer(u'"><img src = "/reject.png"/>\n                </a>\n            </tr>\n')
            __M_writer(u'    </table>\n')
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'edit tags')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "37": 1, "38": 2, "39": 16, "40": 17, "41": 17, "42": 17, "43": 20, "44": 20, "45": 20, "46": 20, "47": 26, "48": 40, "49": 41, "50": 42, "51": 42, "52": 45, "53": 48, "54": 49, "55": 54, "56": 55, "57": 55, "58": 55, "59": 56, "60": 56, "61": 57, "62": 57, "63": 58, "64": 58, "65": 58, "66": 58, "67": 62, "68": 64, "74": 2, "78": 2, "84": 78}, "uri": "/reviews/edit_tags.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/edit_tags.mako"}
__M_END_METADATA
"""
