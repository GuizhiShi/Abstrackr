# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634859.076811
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/merge_reviews.mako'
_template_uri = '/reviews/merge_reviews.mako'
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
        __M_writer(u'\n')
        __M_writer(u'\n<script language="JavaScript">\n    $(document).ready(function() { \n        $( "#dialog" ).dialog({\n            height: 250,\n            width: 400,\n            modal: true,\n            autoOpen: false,   \n            show: "blind",\n        });\n\n        jQuery("#post").click(function(){\n            $("#dialog" ).dialog( "open" );\n        });\n  });\n\n</script>\n\n<div id="dialog" >\n  \n    <h2>merging your reviews. </h2>\n    This may take a while. Maybe get some coffee.<br/><br/>\n    <center>\n    <img src="../../loading.gif"></img>\n    </center>\n</div>\n\n<h1>merge reviews</h1>\n\n<div class="content">\n\n<h2>projects to merge:</h2>\n\n<center>\n<table class="form_table">\n\n ')
        __M_writer(escape(h.form(url(controller='review', action='merge_reviews'), multipart=True, id="merge_review_form",  method='post')))
        __M_writer(u'\n    \n')
        for review in c.reviews:
            __M_writer(u'        <tr><td><input type="checkbox" name="merge_review" value="')
            __M_writer(escape(review.id))
            __M_writer(u'" checked="no"/> ')
            __M_writer(escape(review.name))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'    \n    <tr><td><label>merged project name:</td><td> ')
        __M_writer(escape(h.text('name')))
        __M_writer(u'</label></td></tr>\n\n    <tr><td><label>merged project description:</td> <td>')
        __M_writer(escape(h.textarea('description', rows="10", cols="40")))
        __M_writer(u'</label></td></tr>\n\n\n    <tr><td><label>merged screening mode (<a href="#" id="screen-mode-link">what?</a>):</td> <td>')
        __M_writer(escape(h.select("screen_mode", None, ["Single-screen", "Double-screen", "Advanced"])))
        __M_writer(u' </label></td></tr>\n\n    <tr><td><label>order abstracts by:</td> <td>')
        __M_writer(escape(h.select("order", None, ["Random", "Most likely to be relevant", "Most ambiguous"])))
        __M_writer(u' </label></td></tr>\n    \n    <tr><td><label>pilot round size:</td><td> ')
        __M_writer(escape(h.text('init_size', '0')))
        __M_writer(u'</label></td></tr>\n\n    <tr><td><label>tag visibility (<a href="#" id="tag-visibility-link">what?</a>):</td> <td>')
        __M_writer(escape(h.select("tag_visibility", None, ["Private", "Public"])))
        __M_writer(u' </label></td></tr>\n\n    <div class="actions">\n\n    <tr></tr>\n\n    <tr><td></td><td class="actions"> \n    ')
        __M_writer(escape(h.submit('post', 'merge reviews')))
        __M_writer(u'</td></tr>\n    </div>\n  ')
        __M_writer(escape(h.end_form()))
        __M_writer(u' \n</table>\n</center>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'abstrackr: merge reviews')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 2, "37": 38, "38": 38, "39": 40, "40": 41, "41": 41, "42": 41, "43": 41, "44": 41, "45": 43, "46": 44, "47": 44, "48": 46, "49": 46, "50": 49, "51": 49, "52": 51, "53": 51, "54": 53, "55": 53, "56": 55, "57": 55, "58": 62, "59": 62, "60": 64, "61": 64, "67": 2, "71": 2, "77": 71}, "uri": "/reviews/merge_reviews.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/merge_reviews.mako"}
__M_END_METADATA
"""
