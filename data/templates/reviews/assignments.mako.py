# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634206.036092
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/assignments.mako'
_template_uri = '/reviews/assignments.mako'
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
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n<script language="JavaScript">\n    var cal = new CalendarPopup();\n</script>\n\n\n<div class="breadcrumbs">\n<a href="')
        __M_writer(escape(url(controller='account', action='welcome')))
        __M_writer(u'">./dashboard</a>/<a href="')
        __M_writer(escape(url(controller='review', action='show_review', id=c.review.id)))
        __M_writer(u'">')
        __M_writer(escape(c.review.name))
        __M_writer(u'</a>\n</div>\n\n<h1>')
        __M_writer(escape(c.review.name))
        __M_writer(u': administrivia</h1>\n\n<div class="actions">\n    <a href="')
        __M_writer(escape(url(controller='review', action='admin', id=c.review.id)))
        __M_writer(u'">Manage Participants</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='assignments', id=c.review.id)))
        __M_writer(u'">Manage Assignments</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='edit_review', id=c.review.id)))
        __M_writer(u'">Edit Settings</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='render_add_citations', id=c.review.id)))
        __M_writer(u'">Add Citations</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='render_term_upload_page', id=c.review.id)))
        __M_writer(u'">Upload Terms</a>\n</div>\n\n<div class="content">\n\n<h2>existing assignments</h2> \n    <center>\n    <table width=80% class="list_table" align="center>>\n            <tr align="center">\n            <th width="25%">reviewer</th><th span=20>number to screen</th><th>screened so far</th><th width="20%">assigned</th><th width="20%">due</th><th>delete</th>\n            </tr>\n')
        for i,assignment in enumerate(c.assignments):
            __M_writer(u'                <tr>\n                <td>')
            __M_writer(escape(c.reviewer_ids_to_names_d[assignment.user_id]))
            __M_writer(u'</td>     \n')
            if assignment.num_assigned < 0:
                __M_writer(u'                    <td>--</td>\n')
            else:
                __M_writer(u'                    <td>')
                __M_writer(escape(assignment.num_assigned))
                __M_writer(u'</td>\n')
            __M_writer(u'                <td>')
            __M_writer(escape(c.d_completion_status[assignment.id]))
            __M_writer(u'</td>\n')
            if assignment.date_assigned is not None:
                __M_writer(u'                    <td>')
                __M_writer(escape(assignment.date_assigned.month))
                __M_writer(u'/')
                __M_writer(escape(assignment.date_assigned.day))
                __M_writer(u'/')
                __M_writer(escape(assignment.date_assigned.year))
                __M_writer(u'</td>\n')
            if assignment.date_due is not None:
                __M_writer(u'                    <td>')
                __M_writer(escape(assignment.date_due.month))
                __M_writer(u'/')
                __M_writer(escape(assignment.date_due.day))
                __M_writer(u'/')
                __M_writer(escape(assignment.date_due.year))
                __M_writer(u'</td>\n')
            else:
                __M_writer(u'                    <td>N/A</td>\n')
            __M_writer(u'                <td><a href=\n                       "')
            __M_writer(escape(url(controller='review', action='delete_assignment', review_id=c.review.id, assignment_id=assignment.id)))
            __M_writer(u'">\n                       <img src="/delete_sm.png"></img></a>\n                </tr>\n')
        __M_writer(u'    </table>\n    </center>\n<br/><br/>\n\n<h2>create new assignment</h2>\n<center>\n<br/>\n<form name="new_assignment" action="')
        __M_writer(escape(url(controller='review', action='create_assignment', id=c.review.id)))
        __M_writer(u'">\nassign to: <br/><br/>\n')
        for reviewer in c.participating_reviewers:
            __M_writer(u'    <input type="checkbox" name="assign_to" value="')
            __M_writer(escape(reviewer.username))
            __M_writer(u'" checked="yes"/> ')
            __M_writer(escape(reviewer.username))
            __M_writer(u'<br/>\n')
        __M_writer(u'<br/><br/>\n<table>\n<tr><td>number of citations for each assignee to screen:</td><td> <INPUT TYPE="text" NAME="n" SIZE=10></td></tr>\n<!-- not actually working yet\n<tr><td>percent of these that should be re-screens:</td><td> <INPUT TYPE="text" NAME="p_rescreen" VALUE="0" SIZE=10></td></tr>\n-->\n<tr><td>due date:</td><td>\n<INPUT TYPE="text" NAME="due_date" VALUE="" SIZE=10>\n<a href="#"\n   onClick="cal.select(document.forms[\'new_assignment\'].due_date,\'anchor1\',\'MM/dd/yyyy\'); return false;"\n   NAME="anchor1" ID="anchor1">select</A> </td></tr>\n  <tr><td></td><td class="actions"><INPUT TYPE=SUBMIT VALUE="create assignment"></td></tr>\n</table>\n</form>\n</center>\n\n\n</div>\n')
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
{"source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 2, "37": 3, "38": 10, "39": 10, "40": 10, "41": 10, "42": 10, "43": 10, "44": 13, "45": 13, "46": 16, "47": 16, "48": 17, "49": 17, "50": 18, "51": 18, "52": 19, "53": 19, "54": 20, "55": 20, "56": 31, "57": 32, "58": 33, "59": 33, "60": 34, "61": 35, "62": 36, "63": 37, "64": 37, "65": 37, "66": 39, "67": 39, "68": 39, "69": 40, "70": 41, "71": 41, "72": 41, "73": 41, "74": 41, "75": 41, "76": 41, "77": 43, "78": 44, "79": 44, "80": 44, "81": 44, "82": 44, "83": 44, "84": 44, "85": 45, "86": 46, "87": 48, "88": 49, "89": 49, "90": 53, "91": 60, "92": 60, "93": 62, "94": 63, "95": 63, "96": 63, "97": 63, "98": 63, "99": 65, "105": 3, "110": 3, "116": 110}, "uri": "/reviews/assignments.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/assignments.mako"}
__M_END_METADATA
"""
