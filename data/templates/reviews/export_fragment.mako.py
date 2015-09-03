# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440633848.328591
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/export_fragment.mako'
_template_uri = '/reviews/export_fragment.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<script type="text/javascript">\n\t$(document).ready(function() { \n\t\t$("#export_btn").unbind();\n\n\t    $("#export_btn").click(function()\n\t    {\n\t       \n\t       // now add all selected tags to the study\n\t       var fields = $.map($(\'.ui-selected, this\'), function(element, i) {  \n\t         return $(element).text();  \n\t       });\n\n\n\t\t   $("#export").load(\'/exporting.html\', function(){\n\t       \t\t$("#export").load("')
        __M_writer(escape('/review/export_labels/%s' % c.review_id))
        __M_writer(u'", {fields: fields});\n\t       });\n\t       \n\t       \n\t    });\n\t });\n</script>\n\n<h1>export labels</h1>\n\nselect the fields you\'d like to export:<br/>\n\n<center>\n<ul id="selectable" class="ui-selectable">\n')
        for field in ["(internal) id", "(source) id", "pubmed id"]:
            __M_writer(u' \t<li class="ui-selected">')
            __M_writer(escape(field))
            __M_writer(u'</li>\n')
        __M_writer(u'\n')
        for field in ["keywords", "abstract", "title", "journal", "authors", "tags", "notes"]:
            __M_writer(u'\t<li class="ui-selectee">')
            __M_writer(escape(field))
            __M_writer(u'</li>\n')
        __M_writer(u'</ul>\n\n</center>\n<br/>\n<div class="actions">\n<input id="export_btn" type="button" value="export" />\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 34, "33": 34, "34": 36, "40": 34, "16": 0, "22": 1, "23": 15, "24": 15, "25": 29, "26": 30, "27": 30, "28": 30, "29": 32, "30": 33, "31": 34}, "uri": "/reviews/export_fragment.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/export_fragment.mako"}
__M_END_METADATA
"""
