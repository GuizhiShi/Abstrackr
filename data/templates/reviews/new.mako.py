# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438843801.256809
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/new.mako'
_template_uri = '/reviews/new.mako'
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
        __M_writer(u'\n\n<script language="javascript">\n\n    $(document).ready(function() { \n\n        // fix for issue #4\n        $("input:submit").attr("disabled",true);\n\n        $("input:file").change(function() {\n            if ( $(this).val() && ($.trim($("#name").val()) != "") && ($("#name").val() != null) ) {\n                $("input:submit").attr("disabled",false);\n                $("#select-file").hide();\n            }\n            else\n            {\n                $("input:submit").attr("disabled","disabled");\n                $("#select-file").show();\n            }\n        });\n\n        // Enable the \'Create New Review\' button after the user enters a project name and a file to upload\n        $("#name").keyup(function() {\n            if ( ($.trim($(this).val()) != "") && ($(this).val() != null) && $("input:file").val() ) {\n                $("input:submit").attr("disabled",false);\n                $("#select-file").hide();\n            }\n            else\n            {\n                $("input:submit").attr("disabled","disabled");\n                $("#select-file").show();\n            }\n        });\n\n        $( "#dialog" ).dialog({\n            height: 250,\n            width: 400,\n            modal: true,\n            autoOpen: false,\n            show: "blind",\n        });\n\n        $( "#upload-help" ).dialog({\n            height: 300,\n            width:500, \n            modal: false,\n            autoOpen: false,\n            show: "blind",\n        });\n\n        $( "#train-round-help" ).dialog({\n            height: 200,\n            width:500, \n            modal: false,\n            autoOpen: false,\n            show: "blind",\n        });\n\n        $( "#screen-mode-help" ).dialog({\n            height: 400,\n            width:500, \n            modal: false,\n            autoOpen: false,\n            show: "blind",\n        });\n\n        $( "#tag-visibility-help" ).dialog({\n            height: 200,\n            width:300, \n            modal: false,\n            autoOpen: false,\n            show: "blind",\n        });\n\n\n        $("#post").click(function(){\n            $("#dialog").dialog( "open" );\n        });\n\n        jQuery("#help-link").click(function(){\n            $("#upload-help" ).dialog( "open" );\n        });\n\n        jQuery("#train-round-link").click(function(){\n            $("#train-round-help" ).dialog( "open" );\n        });\n\n        jQuery("#screen-mode-link").click(function(){\n            $("#screen-mode-help" ).dialog( "open" );\n        });\n\n        jQuery("#tag-visibility-link").click(function(){\n            $("#tag-visibility-help" ).dialog( "open" );\n        });\n\n    });\n\n</script>\n\n\n<div id="dialog" >\n    <h2>processing your abstracts. </h2>\n    This may take a while -- please don\'t navigate away from this page.<br/><br/>\n    <center>\n    <img src="/loading.gif"></img>\n    </center>\n</div>\n\n<div id="train-round-help" class="ui-dialog">\n    In a <b>pilot round</b>, everyone screens the same abstracts. Conflicts can then be reviewed by the project lead. The number of abstracts to be screened can be specified here. If you set this, for example, to 100, then everyone will receive the same first 100 abstracts to screen. If you don\'t want a training round, just leave this be at 0.\n</div>\n\n<div id="screen-mode-help" class="ui-dialog">\n    <p>The <b>screening mode</b> specifies how work is to be assigned to participants. </p>\n\n    <p>In the simplest case, <b>single-screen</b>, all abstracts will be screened once. In this mode, participants (reviewers) can screen all they want, until there are no remaining abstracts. If you want people to screen a certain number of abstracts in this mode, simply tell them to stop after they\'ve screened this many. </p>\n\n    <p><b>double-screen</b> behaves analogously, with the exception that every abstract will be screened twice. Individual reviewers will <b>not</b>, however, re-screen the same abstract.</p>\n\n    <p>In <b>advanced</b> mode, you will use the <b>assignments</b> tab to manually assign work to reviewers. At current, this mode only supports single-screening; there is no way to specify that abstracts are to be re-screened.</p>\n\n    <p>Note that regardless of the screening mode, if an initial round size of <i>n</i>    &gt; 0 is specified, <b>all</b> reviewers will screen these <i>n</i> abstracts. </p>\n</div>\n\n<div id="upload-help" class="ui-dialog">\n    You can import a few different file types into <b>abstrackr</b>.<br/>\n\n    <p>The easiest (and suggested!) file format is a list of PubMed IDs, one-per line. Such a list can be exported directly from the PubMed search results page as follows. Click <b>Send to</b>, then select <b>PMID List</b> as the <b>Format</b>. <b>abstrackr</b> will fetch the corresponding titles and abstracts for each id.</p>\n\n    <p>Alternatively, <b>abstrackr</b> can import arbitrary tab-separated files. More specifically, this requires that you create a <b>header row</b> specifying which field each row contains. To this end, <b>abstrackr</b> recognizes special fields; it\'s important that you use the exact same spellings and capitalizations (all lower case) shown here.</p>\n\n    <p>The following fields are mandatory, i.e., must be present in the header row (\\t denotes a tab character):</p>\n    <center><b>id</b> \\t <b>title</b> \\t <b>abstract</b></center>\n\n    <p>Though the abstract for any given citation may be empty. The <b>id</b> may be anything you\'d like to use to identify your citations, though it must be unique for each (i.e., no two rows may have the same <b>id</b>. Additional fields that may be optionally uploaded are:</p>\n\n    <center><b>keywords</b> \\t <b>authors</b> \\t <b>journal</b></center>\n\n    <p>Finally, you may also import XML files exported from the <b>Reference Manager</b> (Versions 11 and 12 are supported) citation software.</p>\n</div>\n\n<div id="tag-visibility-help" class="ui-dialog">\n    <p>By default, the tags are set to be visible <i>only</i> to the project leader.  They are <b>private</b> to the other members of the project, i.e. only project lead and the user himself, if the tag was introduced by a non-leading member, can see the tag.</p>\n    <p>This <b>tag visibility</b> option lets you change the visibility of tags to <b>public</b> or keep it <b>private</b>.  If the tags are public, everyone can see each other\'s tags for any given citation.\n</div>\n\n\n<div class="content">\n    <center>\n        <table class="form_table">\n\n            ')
        __M_writer(escape(h.form(url(controller='review', action='create_review_handler'), multipart=True, id="new_project_form",  method='post')))
        __M_writer(u'\n\n            <tr><td><label>project name:</td><td> ')
        __M_writer(escape(h.text('name', "Review " + c.review_count)))
        __M_writer(u'</label></td></tr>\n\n            <tr><td><label>project description:</td> <td>')
        __M_writer(escape(h.textarea('description', rows="10", cols="40")))
        __M_writer(u'</label></td></tr>\n\n            <tr><td><label>upload file (<a href="#" id="help-link">what can I import?</a>):</label></td> <td>')
        __M_writer(escape(h.file('db')))
        __M_writer(u' </td></tr>\n\n            <tr><td><label>screening mode (<a href="#" id="screen-mode-link">what?</a>):</td> <td>')
        __M_writer(escape(h.select("screen_mode", None, ["Single-screen", "Double-screen", "Advanced"])))
        __M_writer(u' </label></td></tr>\n\n            <tr><td><label>order abstracts by:</td> <td>')
        __M_writer(escape(h.select("order", None, ["Most likely to be relevant", "Random", "Most ambiguous"])))
        __M_writer(u' </label></td></tr>            \n\n            <tr><td><label>pilot round size (<a href="#" id="train-round-link">huh?</a>):</td><td> ')
        __M_writer(escape(h.text('init_size', '0')))
        __M_writer(u'</label></td></tr>\n\n            <tr><td><label>tag visibility (<a href="#" id="tag-visibility-link">what?</a>):</td> <td>')
        __M_writer(escape(h.select("tag_visibility", None, ["Private", "Public"])))
        __M_writer(u' </label></td></tr>\n\n            <!--\n            <tr><td><label>minimum number of abstracts to screen:</td><td> ')
        __M_writer(escape(h.text('min_citations', '0')))
        __M_writer(u'</label></td></tr>\n\n            <tr><td><label>maximum number of abstracts to screen:</td><td> ')
        __M_writer(escape(h.text('max_citations', '0')))
        __M_writer(u'</label></td></tr>\n            -->\n\n            <div id=\'create\' class="actions">\n                <tr><td></td><td></td><td class="actions">\n                <a href="')
        __M_writer(escape(url(controller='account', action='back_to_projects')))
        __M_writer(u'">Cancel</a></td>\n                <td id=\'submit-td\' class="actions">')
        __M_writer(escape(h.submit('post', 'Create new review')))
        __M_writer(u'</td></tr>\n            </div>\n\n            ')
        __M_writer(escape(h.end_form()))
        __M_writer(u' \n\n        </table>\n    </center>\n\n    <div id="select-file" align=\'right\'>Before creating a review, you\'ll have to select a file to upload and make sure the project has a name.</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'new review')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 2, "37": 153, "38": 153, "39": 155, "40": 155, "41": 157, "42": 157, "43": 159, "44": 159, "45": 161, "46": 161, "47": 163, "48": 163, "49": 165, "50": 165, "51": 167, "52": 167, "53": 170, "54": 170, "55": 172, "56": 172, "57": 177, "58": 177, "59": 178, "60": 178, "61": 181, "62": 181, "68": 2, "72": 2, "78": 72}, "uri": "/reviews/new.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/new.mako"}
__M_END_METADATA
"""
