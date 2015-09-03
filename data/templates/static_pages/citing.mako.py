# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634259.002066
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/static_pages/citing.mako'
_template_uri = '/static_pages/citing.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n<title>citing abstrackr</title>\n<LINK href="../stylesheet.css" rel="stylesheet" type="text/css">\n <STYLE type="text/css" media="screen">\n#floating_link {\n     position: fixed;\n     left: 0;\n     top: 10px;\n     display: block;\n     width: 170px;\n     height: 20px;\n     text-indent: 0px;\n     border: 1px solid black;\n     background-color: white;\n     font-color: white;\n}\n</STYLE>\n\n</head>\n\n<body>\n\n\n<a id="floating_link" href="')
        __M_writer(escape(c.root_path))
        __M_writer(u'">&larr; go back to <b>abstrackr</b></a>\n<br/><br/><br/>\n<div class="content">\n\n<p>If you use <b>abstrackr</b> for your project and subsequently publish, please consider citing us using the following citation:</p>\n\n<p><font size="3">Byron C. Wallace, Kevin Small, Carla E. Brodley, Joseph Lau and Thomas A. Trikalinos. <b>Deploying an interactive machine learning system in an evidence-based practice center: abstrackr</b>. In <i>Proc. of the ACM International Health Informatics Symposium (IHI)</i>, p.819--824. 2012.</font>\n\n<p>Questions, kudos and gripes should be sent to <a href="http://tuftscaes.org/byron">Byron Wallace</a> (byron.wallace@gmail.com).</p>\n</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "24": 25, "30": 24, "22": 1, "23": 25}, "uri": "/static_pages/citing.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/static_pages/citing.mako"}
__M_END_METADATA
"""
