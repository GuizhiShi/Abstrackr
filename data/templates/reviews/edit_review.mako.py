# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634213.253499
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/edit_review.mako'
_template_uri = '/reviews/edit_review.mako'
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
        dir = context.get('dir', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<script language="javascript">\njQuery(document).ready(function(){\n    jQuery("#post").click(function(){\n        $("#dialog" ).dialog( "open" );\n        $("#okay_div").fadeIn(2000)\n    });\n\n    $( "#dialog" ).dialog({\n        height: 250,\n        width: 400,\n        modal: true,\n        autoOpen: false,   \n        show: "blind",\n    });\n\n\n    $( "#train-round-help" ).dialog({\n        height: 200,\n        width:500, \n        modal: false,\n        autoOpen: false,\n        show: "blind",\n    });\n\n    $( "#screen-mode-help" ).dialog({\n        height: 400,\n        width:500, \n        modal: false,\n        autoOpen: false,\n        show: "blind",\n    });\n\n    $( "#tag-visibility-help" ).dialog({\n        height: 200,\n        width:300, \n        modal: false,\n        autoOpen: false,\n        show: "blind",\n    });\n\n    jQuery("#train-round-link").click(function(){\n        $("#train-round-help" ).dialog( "open" );\n    });\n\n    jQuery("#screen-mode-link").click(function(){\n        $("#screen-mode-help" ).dialog( "open" );\n    });\n\n    jQuery("#tag-visibility-link").click(function(){\n        $("#tag-visibility-help" ).dialog( "open" );\n    });\n\n});\n\n</script>\n\n<div class="breadcrumbs">\n./<a href="')
        __M_writer(escape(url(controller='account', action='my_projects')))
        __M_writer(u'">my projects</a>/<a href="')
        __M_writer(escape(url(controller='review', action='show_review', id=c.review.id)))
        __M_writer(u'">')
        __M_writer(escape(c.review.name))
        __M_writer(u'</a>\n</div>\n\n<div id="train-round-help" class="ui-dialog">\nIn a <b>pilot round</b>, everyone screens the same abstracts. Conflicts can then be reviewed by the project lead. The number of abstracts to be screened can be specified here. If you set this, for example, to 100, then everyone will receive the same first 100 abstracts to screen. If you don\'t want a training round, just leave this be at 0.\n</div>\n\n\n<div id="screen-mode-help" class="ui-dialog">\n    <p>The <b>screening mode</b> specifies how work is to be assigned to participants. </p>\n\n    <p>In the simplest case, <b>single-screen</b>, all abstracts will be screened once. In this mode, participants (reviewers) can screen all they want, until there are no remaining abstracts. If you want people to screen a certain number of abstracts in this mode, simply tell them to stop after they\'ve screened this many. </p>\n\n    <p><b>double-screen</b> behaves analogously, with the exception that every abstract will be screened twice. Individual reviewers will <b>not</b>, however, re-screen the same abstract.</p>\n\n    <p>In <b>advanced</b> mode, you will use the <b>assignments</b> tab to manually assign work to reviewers. At current, this mode only supports single-screening; there is no way to specify that abstracts are to be re-screened.</p>\n\n    <p>Note that regardless of the screening mode, if an initial round size of <i>n</i>    &gt; 0 is specified, <b>all</b> reviewers will screen these <i>n</i> abstracts. </p>\n</div>\n\n\n<div id="tag-visibility-help" class="ui-dialog">\n    <p>By default, the tags are set to be visible <i>only</i> to the project leader.  They are <b>private</b> to the other members of the project, i.e. only project lead and the user himself, if the tag was introduced by a non-leading member, can see the tag.</p>\n    <p>This <b>tag visibility</b> option lets you change the visibility of tags to <b>public</b> or keep it <b>private</b>.  If the tags are public, everyone can see each other\'s tags for any given citation.\n</div>\n\n\n<div id="dialog" >\n    <h2>Processing your edits... </h2>\n    This may take some time -- please don\'t navigate away from this page.<br/><br/>\n    <center>\n        <img src="../../loading.gif"></img>\n    </center>\n</div>\n\n\n\n<h1>')
        __M_writer(escape(c.review.name))
        __M_writer(u': administrivia</h1>\n<div class="actions">\n    <a href="')
        __M_writer(escape(url(controller='review', action='admin', id=c.review.id)))
        __M_writer(u'">Manage Participants</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='assignments', id=c.review.id)))
        __M_writer(u'">Manage Assignments</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='edit_review', id=c.review.id)))
        __M_writer(u'">Edit Settings</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='render_add_citations', id=c.review.id)))
        __M_writer(u'">Add Citations</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='render_term_upload_page', id=c.review.id)))
        __M_writer(u'">Upload Terms</a>\n</div>\n\n<div class="content">\n\n\n<center>\n<table class="form_table">\n ')
        __M_writer(escape(h.form(url(controller='review', action='edit_review_settings', id=c.review.id), multipart=True, id="edit_project_form",  method='post')))
        __M_writer(u'\n\n    <tr><td><label>screening mode (<a href="#" id="screen-mode-link">what?</a>):</td> <td>')
        __M_writer(escape(h.select("screen_mode", c.screening_mode, ["Single-screen", "Double-screen", "Advanced"])))
        __M_writer(u' </label></td></tr>\n\n    <tr><td><label>order abstracts by:</td> <td>')
        __M_writer(escape(h.select("order", c.order_abstracts, ["Most likely to be relevant", "Random", "Most ambiguous"])))
        __M_writer(u' </label></td></tr>\n    \n     <tr><td><label>pilot round size (<a href="#" id="train-round-link">what?</a>):</td><td> ')
        __M_writer(escape(h.text('init_size', c.review.initial_round_size)))
        __M_writer(u'</label></td></tr>\n\n    <tr><td><label>tag visibility (<a href="#" id="tag-visibility-link">what?</a>):</td> <td>')
        __M_writer(escape(h.select("tag_visibility", c.tag_privacy, ["Private", "Public"])))
        __M_writer(u' </label></td></tr>\n    \n    <div class="actions">\n    <tr><td></td><td></td><td class="actions"> \n    <td class="actions">')
        __M_writer(escape(h.submit('post', 'Apply to review')))
        __M_writer(u'</td></tr>\n    </div>\n  ')
        __M_writer(escape(h.end_form()))
        __M_writer(u' \n</table>\n</center>\n\n')
        if 'msg' in dir(c):
            __M_writer(u'        <div id="okay_div"><font color=\'green\'>')
            __M_writer(escape(c.msg))
            __M_writer(u'</font>\n        </div>\n')
        __M_writer(u'\n</div>\n')
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
{"source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 3, "39": 62, "40": 62, "41": 62, "42": 62, "43": 62, "44": 62, "45": 99, "46": 99, "47": 101, "48": 101, "49": 102, "50": 102, "51": 103, "52": 103, "53": 104, "54": 104, "55": 105, "56": 105, "57": 113, "58": 113, "59": 115, "60": 115, "61": 117, "62": 117, "63": 119, "64": 119, "65": 121, "66": 121, "67": 125, "68": 125, "69": 127, "70": 127, "71": 131, "72": 132, "73": 132, "74": 132, "75": 135, "81": 3, "86": 3, "92": 86}, "uri": "/reviews/edit_review.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/edit_review.mako"}
__M_END_METADATA
"""
