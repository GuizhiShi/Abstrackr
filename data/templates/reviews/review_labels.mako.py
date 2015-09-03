# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440633716.751578
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/review_labels.mako'
_template_uri = '/reviews/review_labels.mako'
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
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n\n\n')
        if c.assignment is not None:
            __M_writer(u'<div class = "actions">\n    <a href="')
            __M_writer(escape(url(controller='review', action='screen', review_id=c.assignment.project_id, assignment_id=c.assignment.id)))
            __M_writer(u'">ok, get back to screening <img src="../../arrow_right.png"></img></a>\n    </div>\n')
        __M_writer(u'\n\n<div class="content">\n<div id="labels_fragment">\n')
        if len(c.given_labels) > 0:
            __M_writer(u'    labels you\'ve provided: <br/><br/>\n    <center>\n    <table width=100% class="list_table" align="center>>\n            <tr align="center">\n            \n            <th span=20>doc id</th>\n            <th span=20>refman id</th>\n            <th span=20>pubmed id</th>\n            <th width="30%">title</th>\n            <th>label</th>\n            <th>first labeled</th>\n            <th>last updated</th>\n            \n            </tr>\n')
            for i, label in enumerate(c.given_labels):
                __M_writer(u'                <tr>\n                <td>')
                __M_writer(escape(label.study_id))
                __M_writer(u'</td>\n                <td>')
                __M_writer(escape(c.citations_d[label.study_id].refman))
                __M_writer(u'</td>\n                <td>')
                __M_writer(escape(c.citations_d[label.study_id].pmid))
                __M_writer(u'</td>\n                <td>\n               \n                <a href="')
                __M_writer(escape(url(controller='review', action='show_labeled_citation', review_id=label.project_id, citation_id=label.study_id, assignment_id=label.assignment_id)))
                __M_writer(u'">')
                __M_writer(escape(c.citations_d[label.study_id].title))
                __M_writer(u'</a></td>\n\n                <td>')
                __M_writer(escape(label.label))
                __M_writer(u'</td>\n                <td>')
                __M_writer(escape(label.first_labeled.month))
                __M_writer(u'/')
                __M_writer(escape(label.first_labeled.day))
                __M_writer(u'/')
                __M_writer(escape(label.first_labeled.year))
                __M_writer(u'</td>\n                <td>')
                __M_writer(escape(label.label_last_updated.month))
                __M_writer(u'/')
                __M_writer(escape(label.label_last_updated.day))
                __M_writer(u'/')
                __M_writer(escape(label.label_last_updated.year))
                __M_writer(u'</td>\n                <td></td>\n                </tr>\n')
            __M_writer(u'    </table>\n    </center>\n')
        else:
            __M_writer(u"    whoops, you've not labeled anything yet. \n")
        __M_writer(u'</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'review labels')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 6, "39": 7, "40": 8, "41": 8, "42": 11, "43": 15, "44": 16, "45": 30, "46": 31, "47": 32, "48": 32, "49": 33, "50": 33, "51": 34, "52": 34, "53": 37, "54": 37, "55": 37, "56": 37, "57": 39, "58": 39, "59": 40, "60": 40, "61": 40, "62": 40, "63": 40, "64": 40, "65": 41, "66": 41, "67": 41, "68": 41, "69": 41, "70": 41, "71": 45, "72": 47, "73": 48, "74": 50, "80": 2, "84": 2, "90": 84}, "uri": "/reviews/review_labels.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/review_labels.mako"}
__M_END_METADATA
"""
