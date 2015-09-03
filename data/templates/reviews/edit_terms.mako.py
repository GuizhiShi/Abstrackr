# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438909698.110444
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/edit_terms.mako'
_template_uri = '/reviews/edit_terms.mako'
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
        c = context.get('c', UNDEFINED)
        zip = context.get('zip', UNDEFINED)
        url = context.get('url', UNDEFINED)
        len = context.get('len', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        dir = context.get('dir', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if "assignment" in dir(c) and c.assignment is not None:
            __M_writer(u'  <div class = "actions">\n      <a href="')
            __M_writer(escape(url(controller='review', action='screen', review_id=c.assignment.project_id, assignment_id=c.assignment.id)))
            __M_writer(u'">ok, get back to screening <img src="../../../arrow_right.png"></img></a>\n      </div>\n')
        __M_writer(u'\n<div class="content">\n')
        if len(c.terms) > 0:
            __M_writer(u'    terms you\'ve labeled: <br/><br/>\n    <table class="list_table">\n        <th>term</th>\n        <th>current label</th>\n        <th>delete</th>\n        <th>re-label</th>\n')
            for i,term in enumerate(c.terms):
                __M_writer(u'            <tr class="')
                __M_writer(escape('odd' if i%2 else 'even'))
                __M_writer(u'">\n              <td>')
                __M_writer(escape(term.term))
                __M_writer(u'</td>           \n              <td><img src="/')
                __M_writer(escape(dict(zip([-2, -1, 1, 2],["two_thumbs_down.png", "thumbs_down.png", "thumbs_up.png", "two_thumbs_up.png"]))[term.label]))
                __M_writer(u'"></td> \n              <td><a href="/review/delete_term/')
                __M_writer(escape(term.id))
                __M_writer(u'/')
                __M_writer(escape(c.assignment.id))
                __M_writer(u'"><img src = "/reject.png"/></a> </td>\n              <td>\n                    <a href="/relabel_term/')
                __M_writer(escape(term.id))
                __M_writer(u'/')
                __M_writer(escape(c.assignment.id))
                __M_writer(u'/1"><img src = "/thumbs_up.png" border="2" alt="indicative of relevance"></a>\n                    <a href="/relabel_term/')
                __M_writer(escape(term.id))
                __M_writer(u'/')
                __M_writer(escape(c.assignment.id))
                __M_writer(u'/2"><img src = "/two_thumbs_up.png" border="2" alt="strongly indicative of relevance"></a>\n                    <a href="/relabel_term/')
                __M_writer(escape(term.id))
                __M_writer(u'/')
                __M_writer(escape(c.assignment.id))
                __M_writer(u'/-1"><img src = "/thumbs_down.png"/ border="2" alt="indicative of irrelevance" ></a>\n                    <a href="/relabel_term/')
                __M_writer(escape(term.id))
                __M_writer(u'/')
                __M_writer(escape(c.assignment.id))
                __M_writer(u'/-2"><img src = "/two_thumbs_down.png"/ border="2" alt="strongly indicative of irrelevance"></a>\n              </td>\n            </tr>\n')
            __M_writer(u'    </table>\n')
        else:
            __M_writer(u"   you haven't labeled any terms for this project yet. (in the future, I'll suggest some...)\n")
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'edit terms')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "39": 1, "40": 2, "41": 4, "42": 5, "43": 6, "44": 6, "45": 9, "46": 11, "47": 12, "48": 18, "49": 19, "50": 19, "51": 19, "52": 20, "53": 20, "54": 21, "55": 21, "56": 22, "57": 22, "58": 22, "59": 22, "60": 24, "61": 24, "62": 24, "63": 24, "64": 25, "65": 25, "66": 25, "67": 25, "68": 26, "69": 26, "70": 26, "71": 26, "72": 27, "73": 27, "74": 27, "75": 27, "76": 31, "77": 32, "78": 33, "79": 35, "85": 2, "89": 2, "95": 89}, "uri": "/reviews/edit_terms.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/reviews/edit_terms.mako"}
__M_END_METADATA
"""
