# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634216.661257
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/add_citations.mako'
_template_uri = '/reviews/add_citations.mako'
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
        __M_writer(u'\n\n<script language="javascript">\n    jQuery(document).ready(function(){\n        \n        /*$("input:submit").attr("disabled",true);\n\n        $("input:file").change(function() {\n            if ( $(this).val() && ($.trim($("#name").val()) != "") && ($("#name").val() != null) ) \n            {\n                $("input:submit").attr("disabled",false);\n                $("#select-file").hide();\n            }\n        });*/\n\n        jQuery("#post").click(function(){\n        \t$("#dialog" ).dialog( "open" );\n            $("#okay_div").fadeIn(2000)\n        });\n\n        $( "#dialog" ).dialog({\n            height: 250,\n            width: 400,\n            modal: true,\n            autoOpen: false,   \n            show: "blind",\n        });\n\n        $( "#upload-help" ).dialog({\n            height: 300,\n            width:500, \n            modal: false,\n            autoOpen: false,\n            show: "blind",\n        });\n\n        jQuery("#help-link").click(function(){\n            $("#upload-help" ).dialog( "open" );\n        });\n\n    });\n\n</script>\n\n<div class="breadcrumbs">\n    ./<a href="')
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
        __M_writer(u'">Upload Terms</a>\n</div>\n\n<div id="upload-help" class="ui-dialog">\n    You can import a few different file types into <b>abstrackr</b>.<br/>\n\n    <p>The easiest (and suggested!) file format is a list of PubMed IDs, one-per line. Such a list can be exported directly from the PubMed search results page as follows. Click <b>Send to</b>, then select <b>PMID List</b> as the <b>Format</b>. <b>abstrackr</b> will fetch the corresponding titles and abstracts for each id.</p>\n\n    <p>Alternatively, <b>abstrackr</b> can import arbitrary tab-separated files. More specifically, this requires that you create a <b>header row</b> specifying which field each row contains. To this end, <b>abstrackr</b> recognizes special fields; it\'s important that you use the exact same spellings and capitalizations (all lower case) shown here.</p>\n\n    <p>The following fields are mandatory, i.e., must be present in the header row (\\t denotes a tab character):</p>\n    <center><b>id</b> \\t <b>title</b> \\t <b>abstract</b></center>\n\n    <p>Though the abstract for any given citation may be empty. The <b>id</b> may be anything you\'d like to use to identify your citations, though it must be unique for each (i.e., no two rows may have the same <b>id</b>. Additional fields that may be optionally uploaded are:</p>\n\n    <center><b>keywords</b> \\t <b>authors</b> \\t <b>journal</b></center>\n\n    <p>Finally, you may also import XML files exported from the <b>Reference Manager</b> (Versions 11 and 12 are supported) citation software.</p>\n</div>\n\n<div class="content">\n\n    <center>\n        <table class="form_table">\n            ')
        __M_writer(escape(h.form(url(controller='review', action='add_citations', id=c.review.id), multipart=True, id="add_citations_form",  method='post')))
        __M_writer(u'\n                \n                <tr><td><label>Upload Citation-File (<a href="#" id="help-link">what can I upload?</a>):</label></td> <td>')
        __M_writer(escape(h.file('db')))
        __M_writer(u' </td></tr>\n\n                <div class="actions">\n                    <tr><td></td><td></td><td class="actions"> \n                    <td class="actions">')
        __M_writer(escape(h.submit('post', 'Add to Review')))
        __M_writer(u'</td></tr>\n                </div>\n            ')
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n        </table>\n    </center>\n\n')
        if 'msg' in dir(c):
            __M_writer(u'\t\t<div id="okay_div"><font color=\'green\'>')
            __M_writer(escape(c.msg))
            __M_writer(u'</font>\n\t \t</div>\n')
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
{"source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 3, "39": 48, "40": 48, "41": 48, "42": 48, "43": 48, "44": 48, "45": 61, "46": 61, "47": 63, "48": 63, "49": 64, "50": 64, "51": 65, "52": 65, "53": 66, "54": 66, "55": 67, "56": 67, "57": 91, "58": 91, "59": 93, "60": 93, "61": 97, "62": 97, "63": 99, "64": 99, "65": 103, "66": 104, "67": 104, "68": 104, "69": 107, "75": 3, "80": 3, "86": 80}, "uri": "/reviews/add_citations.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/add_citations.mako"}
__M_END_METADATA
"""
