# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440633856.737054
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/download_labels.mako'
_template_uri = '/reviews/download_labels.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<h2>Labels exported!</h2>\n\n<br/>\n\nClick this link to download them:<br/><br/>\n<center>\n<a href="')
        __M_writer(escape(c.download_url))
        __M_writer(u'" onclick="javascript: $(\'#export\').dialog(\'close\');">')
        __M_writer(escape(c.download_url))
        __M_writer(u'</a>\n</center><br/><br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "16": 0, "22": 1, "23": 7, "24": 7, "25": 7, "26": 7}, "uri": "/reviews/download_labels.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/download_labels.mako"}
__M_END_METADATA
"""
