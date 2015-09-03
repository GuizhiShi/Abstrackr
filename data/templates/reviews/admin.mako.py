# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440634191.459593
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/admin.mako'
_template_uri = '/reviews/admin.mako'
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
        __M_writer(u'\n<script language="JavaScript">\n    var cal = new CalendarPopup();\n</script>\n\n<script language="javascript">\n    jQuery(document).ready(function(){\n        jQuery("#submit").click(function(){\n            $("#okay_div").fadeIn(2000)\n        });\n    });\n</script>\n\n<div class="breadcrumbs">\n    ./<a href="')
        __M_writer(escape(url(controller='account', action='my_projects')))
        __M_writer(u'">my projects</a>/<a href="')
        __M_writer(escape(url(controller='review', action='show_review', id=c.review.id)))
        __M_writer(u'">')
        __M_writer(escape(c.review.name))
        __M_writer(u'</a>\n</div>\n\n<h1>')
        __M_writer(escape(c.review.name))
        __M_writer(u': administrivia</h1>\n\n<div class="actions">\n    <a href="')
        __M_writer(escape(url(controller='review', action='admin', project_id=c.review.id)))
        __M_writer(u'">Manage Participants</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='assignments', id=c.review.id)))
        __M_writer(u'">Manage Assignments</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='edit_review', id=c.review.id)))
        __M_writer(u'">Edit Settings</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='render_add_citations', id=c.review.id)))
        __M_writer(u'">Add Citations</a>\n    <a href="')
        __M_writer(escape(url(controller='review', action='render_term_upload_page', id=c.review.id)))
        __M_writer(u'">Upload Terms</a>\n</div>\n\n\n<div class="content">\n\n')
        if len(c.participating_reviewers)>0:
            __M_writer(u'        <h2>Participants</h2>\n        <table class="list_table">\n        <tr align="center"><th>person</th><th></th></tr>\n')
            for participant in c.participating_reviewers:
                __M_writer(u'            <tr>\n                <td>')
                __M_writer(escape(participant.fullname))
                __M_writer(u'</td>\n                <td class="actions">\n                    <a href="/review/remove_from_review/')
                __M_writer(escape(participant.id))
                __M_writer(u'/')
                __M_writer(escape(c.review.id))
                __M_writer(u'">remove from review</a>\n')
                if participant in c.project_leader_list:
                    __M_writer(u'                        <a href="/review/remove_admin/')
                    __M_writer(escape(c.review.id))
                    __M_writer(u'/')
                    __M_writer(escape(participant.id))
                    __M_writer(u'">remove user from project leader group</a>\n')
                else:
                    __M_writer(u'                        <a href="/review/add_admin/')
                    __M_writer(escape(c.review.id))
                    __M_writer(u'/')
                    __M_writer(escape(participant.id))
                    __M_writer(u'">add user to the project leader group</a></td>\n')
                __M_writer(u'                </td>\n            </tr>\n')
            __M_writer(u'        </table>\n        <br/>\n')
        elif c.admin_msg == "":
            __M_writer(u"        <H2>Hrmm... You're the only person participating in this review. </h2><h2>But don't despair: you can invite people below! </H2>\n        <br/><br/>\n")
        __M_writer(u'\n')
        if c.admin_msg != "":
            __M_writer(u'        <H2>')
            __M_writer(escape(c.admin_msg))
            __M_writer(u'</H2>\n')
        __M_writer(u'\n    <div align="right">\n        <form action = "/review/invite_reviewers/')
        __M_writer(escape(c.review.id))
        __M_writer(u'">\n            <div class="actions">\n                <label for="emails">Want to invite additional reviewers? Enter their emails (comma-separated).</label>\n                <input type="text" id="emails" name="emails" /><br />\n                <input type="submit" id="submit" value="invite them" />\n            </div>\n        </form>\n        <div class="loading" id="okay_div">\n            okay! emails have been sent!\n        </div>\n    </div>\n\n    <div class="loading" id="okay_div">\n        okay! emails have been sent!\n    </div>\n\n    <p align="right">\n        Alternatively, they can join the review themselves by following this link: <b>')
        __M_writer(escape(c.root_path))
        __M_writer(u'join/')
        __M_writer(escape(c.review.code))
        __M_writer(u'</b>\n    </p>\n\n</div>\n')
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
{"source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 2, "37": 3, "38": 17, "39": 17, "40": 17, "41": 17, "42": 17, "43": 17, "44": 20, "45": 20, "46": 23, "47": 23, "48": 24, "49": 24, "50": 25, "51": 25, "52": 26, "53": 26, "54": 27, "55": 27, "56": 33, "57": 34, "58": 37, "59": 38, "60": 39, "61": 39, "62": 41, "63": 41, "64": 41, "65": 41, "66": 42, "67": 43, "68": 43, "69": 43, "70": 43, "71": 43, "72": 44, "73": 45, "74": 45, "75": 45, "76": 45, "77": 45, "78": 47, "79": 50, "80": 52, "81": 53, "82": 56, "83": 57, "84": 58, "85": 58, "86": 58, "87": 60, "88": 62, "89": 62, "90": 79, "91": 79, "92": 79, "93": 79, "99": 3, "104": 3, "110": 104}, "uri": "/reviews/admin.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/admin.mako"}
__M_END_METADATA
"""
