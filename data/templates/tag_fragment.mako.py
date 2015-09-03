# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440633593.799827
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/tag_fragment.mako'
_template_uri = '/tag_fragment.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<script>\n    $("#selectable").selectable();\n    setup_submit();\n</script>\n\n')
        if len(c.tags) > 0:
            for i,tag in enumerate(c.tags):
                __M_writer(u'        <li class=')
                __M_writer(escape("tag%s"%(i+1)))
                __M_writer(u'><a href="#">')
                __M_writer(escape(tag))
                __M_writer(u'</a></li>\n')
            __M_writer(u'</ul>\n')
        else:
            __M_writer(u'        (no tags yet.)\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 10, "33": 11, "34": 12, "40": 34, "16": 0, "24": 1, "25": 6, "26": 7, "27": 8, "28": 8, "29": 8, "30": 8, "31": 8}, "uri": "/tag_fragment.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/tag_fragment.mako"}
__M_END_METADATA
"""
