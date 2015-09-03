# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438909536.01898
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/conflict_button.mako'
_template_uri = '/reviews/conflict_button.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        if c.display_the_button:
            __M_writer(u'    <td class="inline-actions"><a href="')
            __M_writer(escape(url(controller='review', action='review_conflicts', id=c.review_id)))
            __M_writer(u'">\n        conflicts<img src = "../../conflicts_sm.png"></a></td>    \n')
        else:
            __M_writer(u'    <td class="inline-actions"><i>no conflicts yet</i></td>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 28, "16": 0, "23": 1, "24": 2, "25": 2, "26": 2, "27": 4, "28": 5}, "uri": "/reviews/conflict_button.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/conflict_button.mako"}
__M_END_METADATA
"""
