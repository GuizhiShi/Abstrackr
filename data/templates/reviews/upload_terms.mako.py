# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634220.737314
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/upload_terms.mako'
_template_uri = '/reviews/upload_terms.mako'
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
        __M_writer(u'\n\n<script language="javascript">\n    jQuery(document).ready(function(){\n        \n        /*$("input:submit").attr("disabled",true);\n\n        $("input:file").change(function() {\n            if ( $(this).val() && ($.trim($("#name").val()) != "") && ($("#name").val() != null) ) \n            {\n                $("input:submit").attr("disabled",false);\n                $("#select-file").hide();\n            }\n        });*/\n\n        jQuery("#post").click(function(){\n          $("#dialog" ).dialog( "open" );\n            $("#okay_div").fadeIn(2000)\n        });\n\n        $( "#dialog" ).dialog({\n            height: 250,\n            width: 400,\n            modal: true,\n            autoOpen: false,   \n            show: "blind",\n        });\n\n        $( "#upload-help" ).dialog({\n            height: 300,\n            width:500, \n            modal: false,\n            autoOpen: false,\n            show: "blind",\n        });\n\n        jQuery("#help-link").click(function(){\n            $("#upload-help" ).dialog( "open" );\n        });\n\n    });\n\n</script>\n\n<div class="breadcrumbs">\n    ./<a href="')
        __M_writer(escape(url(controller='account', action='my_projects')))
        __M_writer(u'">my projects</a>/<a href="')
        __M_writer(escape(url(controller='review', action='show_review', id=c.review.id)))
        __M_writer(u'">')
        __M_writer(escape(c.review.name))
        __M_writer(u'</a>\n</div>\n\n<div id="dialog" >\n    <h2>processing your edits...</h2>\n    This may take some time -- please don\'t navigate away from this page.<br/><br/>\n    <center>\n    <img src="../../loading.gif"></img>\n    </center>\n</div>\n\n\n\n<h1>')
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
        __M_writer(u'">Upload Terms</a>\n</div>\n\n<div id="upload-help" class="ui-dialog">\n    <div>You may import a tab delimited file here. Each line should consist of a term you wish to highlight as well as the rating the term is associated with.</div>\n    <br />\n    <div>A positive numbers indicate positive relevance, while negative numbers indicate negative relevance.</div>\n    <br />\n    <div>Please restrict the rating to 1\'s and 2\'s only, where a positive 1 implies \'relevant\' and a positive 2 means \'very relevant\', a negative 1 implies \'irrelevant\' and a negative 2 means \'very irrelevant\'.</div>\n</div>\n\n<div class="content">\n\n    <center>\n        <table class="form_table">\n            ')
        __M_writer(escape(h.form(url(controller='review', action='upload_terms', id=c.review.id), multipart=True, id="add_terms_form",  method='post')))
        __M_writer(u'\n                \n                <tr><td><label>Upload Terms-File (<a href="#" id="help-link">what can I upload?</a>):</label></td> <td>')
        __M_writer(escape(h.file('db')))
        __M_writer(u' </td></tr>\n\n                <div class="actions">\n                    <tr><td></td><td></td><td class="actions"> \n                    <td class="actions">')
        __M_writer(escape(h.submit('post', 'Add to Review')))
        __M_writer(u'</td></tr>\n                </div>\n            ')
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n        </table>\n    </center>\n\n')
        if 'msg' in dir(c):
            __M_writer(u'    <div id="okay_div"><font color=\'green\'>')
            __M_writer(escape(c.msg))
            __M_writer(u'</font>\n    </div>\n')
        __M_writer(u'\n    <div id="select-file" align=\'right\'>You must select a citation-file to upload in order to \'Add to Review\' .</div>\n\n</div>\n')
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
{"source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 3, "39": 48, "40": 48, "41": 48, "42": 48, "43": 48, "44": 48, "45": 61, "46": 61, "47": 63, "48": 63, "49": 64, "50": 64, "51": 65, "52": 65, "53": 66, "54": 66, "55": 67, "56": 67, "57": 82, "58": 82, "59": 84, "60": 84, "61": 88, "62": 88, "63": 90, "64": 90, "65": 94, "66": 95, "67": 95, "68": 95, "69": 98, "75": 3, "80": 3, "86": 80}, "uri": "/reviews/upload_terms.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/upload_terms.mako"}
__M_END_METADATA
"""
