# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438909675.450374
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/review_created.mako'
_template_uri = '/reviews/review_created.mako'
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
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n<script language="JavaScript">\n    var cal = new CalendarPopup();\n</script>\n\n<script language="javascript">\njQuery(document).ready(function(){\n    jQuery("#submit").click(function(){\n        $("#okay_div").fadeIn(2000)\n    });\n});\n</script>\n\n\n\n\n<h1>Your review (')
        __M_writer(escape(c.review.name))
        __M_writer(u') has been succesfully created!</h1>\n\n<div class="actions">\n\n    <a href="')
        __M_writer(escape(url(controller='account', action='my_work')))
        __M_writer(u'">ok, go to my home screen</a>\n \n</div>\n\n\n<div class="content">\n\nWell done! ')
        __M_writer(escape(c.num_articles))
        __M_writer(u' of ')
        __M_writer(escape(c.num_articles + len(c.flash["import-errors"])))
        __M_writer(u' abstracts have been imported\n\n')
        if len(c.flash["import-errors"])>0:
            __M_writer(u'<div class=flash>\n    We encountered the following problems:\n    <ul>\n')
            for error in c.flash["import-errors"]:
                __M_writer(u'        <div class=import-errors><li>')
                __M_writer(escape(error))
                __M_writer(u'</li></div>\n')
            __M_writer(u'    </ul>\n</div>\n')
        __M_writer(u'\n<br>\nAwesome, you\'re ready to start screening.\n\n<br/><br/>\n<b>What now?</b>, you ask. You can invite additional reviewers, if you\'d like.<br/><br/>\n\n<div align="right">\n<form action = "/review/invite_reviewers/')
        __M_writer(escape(c.review.id))
        __M_writer(u'">\n<div class="actions">\n<label for="emails">Enter their emails (comma-separated).</label>\n<input type="text" id="emails" name="emails" /><br />\n<input type="submit" id="submit" value="invite them!" />\n</div>\n</form>\n    <div class="loading" id="okay_div">\n        okay! emails have been sent!\n    </div>\n</div>\n\n<br/><br/>\nOr, send this link directly to participants:\n\n<center>\n<h2><a href="')
        __M_writer(escape(c.root_path))
        __M_writer(u'join/')
        __M_writer(escape(c.review.code))
        __M_writer(u'">')
        __M_writer(escape(c.root_path))
        __M_writer(u'join/')
        __M_writer(escape(c.review.code))
        __M_writer(u'</a></h2>\n</center>\n\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(escape(c.review.name))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 2, "37": 3, "38": 19, "39": 19, "40": 23, "41": 23, "42": 30, "43": 30, "44": 30, "45": 30, "46": 32, "47": 33, "48": 36, "49": 37, "50": 37, "51": 37, "52": 39, "53": 42, "54": 50, "55": 50, "56": 66, "57": 66, "58": 66, "59": 66, "60": 66, "61": 66, "62": 66, "63": 66, "69": 3, "74": 3, "80": 74}, "uri": "/reviews/review_created.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/review_created.mako"}
__M_END_METADATA
"""
