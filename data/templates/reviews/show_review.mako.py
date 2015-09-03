# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438909689.735831
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/show_review.mako'
_template_uri = '/reviews/show_review.mako'
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
        float = context.get('float', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n\n\n<h1>')
        __M_writer(escape(c.review.name))
        __M_writer(u'</h1>\n\t<div class="actions">\n    <a\n      href="')
        __M_writer(escape(url(controller='review', action='review_labels', review_id=c.review.id)))
        __M_writer(u'">review labels</a>\n    <a \n      href="')
        __M_writer(escape(url(controller='review', action='review_terms', id=c.review.id)))
        __M_writer(u'">review terms</a>\n</div>\n<div class="content">\n<h2>Project description</h2> \n')
        __M_writer(escape(c.review.description))
        __M_writer(u'\n<br/><br/>\n<h2>Progress</h2>\n\n')
        if float(c.num_labels)/float(c.num_citations) >= .1:
            __M_writer(u'\t<center><img src = "')
            __M_writer(escape(c.pi_url))
            __M_writer(u'"></img></center><br/>\n')
        __M_writer(u'\nThere are ')
        __M_writer(escape(c.num_citations))
        __M_writer(u' citations in this review, so far ')
        __M_writer(escape(c.num_labels))
        __M_writer(u' have been labeled.\n<br/><br/>\n\n<h2>Participants</h2>\nThis review is lead by\n<div>\n    <ul>\n')
        for leader in c.project_leaders:
            __M_writer(u'            <li>\n                ')
            __M_writer(escape(leader.fullname))
            __M_writer(u'\n            </li>\n')
        __M_writer(u'    </ul>\n</div>\n<br/>\n')
        if len(c.participating_reviewers) > 1:
            __M_writer(u'    The following people are reviewers on the project: \n')
            for user in c.participating_reviewers[:-1]:
                __M_writer(u'        ')
                __M_writer(escape(user.fullname))
                __M_writer(u',\n')
            __M_writer(u'    and ')
            __M_writer(escape(c.participating_reviewers[-1].fullname))
            __M_writer(u'.\n')
        else:
            __M_writer(u'    This project is a lonely undertaking by ')
            __M_writer(escape(c.participating_reviewers[0].fullname))
            __M_writer(u'.\n')
        __M_writer(u'<br/><br/>\nNumber of citations screened by reviewers:\n<center>\n<img src= "')
        __M_writer(escape(c.workload_graph_url))
        __M_writer(u'">\n</center>\n</div>\n')
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
{"source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 3, "39": 7, "40": 7, "41": 10, "42": 10, "43": 12, "44": 12, "45": 16, "46": 16, "47": 20, "48": 21, "49": 21, "50": 21, "51": 23, "52": 24, "53": 24, "54": 24, "55": 24, "56": 31, "57": 32, "58": 33, "59": 33, "60": 36, "61": 39, "62": 40, "63": 41, "64": 42, "65": 42, "66": 42, "67": 44, "68": 44, "69": 44, "70": 45, "71": 46, "72": 46, "73": 46, "74": 48, "75": 51, "76": 51, "82": 3, "87": 3, "93": 87}, "uri": "/reviews/show_review.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/show_review.mako"}
__M_END_METADATA
"""
