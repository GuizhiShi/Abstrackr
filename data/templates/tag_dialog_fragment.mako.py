# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634991.094334
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/tag_dialog_fragment.mako'
_template_uri = '/tag_dialog_fragment.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<form>\n    <center>\n        new tag: <input type="text" id="new_tag" name="new_tag" /><br />\n    </center>\n    <br/>\n\n    <center>\n        <ul id="selectable" class="ui-selectable">\n')
        for tag in c.tag_types:
            if tag in c.tags:
                __M_writer(u'                    <li class="ui-selected">')
                __M_writer(escape(tag))
                __M_writer(u'</li>\n')
            else:
                __M_writer(u'                    <li>')
                __M_writer(escape(tag))
                __M_writer(u'</li>\n')
        __M_writer(u'        </ul>\n    </center>\n\n    <div class="actions" style="text-align: right;">\n        <input id="submit_btn" type="button" value="tag" />\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 16, "38": 32, "16": 0, "22": 1, "23": 9, "24": 10, "25": 11, "26": 11, "27": 11, "28": 12, "29": 13, "30": 13, "31": 13}, "uri": "/tag_dialog_fragment.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/tag_dialog_fragment.mako"}
__M_END_METADATA
"""
