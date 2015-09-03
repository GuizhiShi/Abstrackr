# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440635048.412506
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/assignment_complete.mako'
_template_uri = '/assignment_complete.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        dir = context.get('dir', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<h2>Huzzah! You\'ve completed this assignment.</h2> <br/></br><h2> Nice work.</h2>\n\n<script type="text/javascript">    \n    function setup_js(){\n\n')
        if not 'assignment' in dir(c):
            if c.assignment.num_assigned and c.assignment.num_assigned > 0:
                __M_writer(u'            $("#progress").html("you\'ve screened <b>')
                __M_writer(escape(c.assignment.done_so_far))
                __M_writer(u'</b> out of <b>')
                __M_writer(escape(c.assignment.num_assigned))
                __M_writer(u'</b> so far (nice going!)");\n')
            else:
                __M_writer(u'            $("#progress").html("you\'ve screened <b>')
                __M_writer(escape(c.assignment.done_so_far))
                __M_writer(u'</b> abstracts thus far, and, regrettably, there are no more for you to screen.");\n')
        else:
            __M_writer(u'          $("#progress").html("");\n')
        __M_writer(u'\n\n        $(\'#buttons\').html("");\n        //alert("???");\n        $(\'#buttons\').remove()\n        $(\'#tags_container\').remove();\n        $(\'#label_terms\').remove();\n        \n    }\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 11, "33": 11, "34": 11, "35": 13, "36": 14, "37": 16, "43": 37, "16": 0, "23": 1, "24": 7, "25": 8, "26": 9, "27": 9, "28": 9, "29": 9, "30": 9, "31": 10}, "uri": "/assignment_complete.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/assignment_complete.mako"}
__M_END_METADATA
"""
