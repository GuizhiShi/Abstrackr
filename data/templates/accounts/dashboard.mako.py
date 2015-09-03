# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438750319.731151
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/dashboard.mako'
_template_uri = '/accounts/dashboard.mako'
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
        __M_writer(u'\n\n\n<script type="text/javascript" src="/scripts/jquery.alerts.js"></script>\n\n<link href="/scripts/jquery.alerts.css"  rel="stylesheet" type="text/css" media="screen" />\n\n<script language="javascript">\n\n    $(document).ready(function() { \n  \n\n        $("#export").dialog({\n            height: 500,\n            width:500, \n            modal: true,\n            autoOpen: false,\n            show: "blind",\n        });\n        \n        \n    });\n\n</script>\n\n\n<div id="export" class="dialog"></div>\n\n<button type="button" onclick="introJs().start()">Quick Tour!</button>\n\t\n')
        if c.my_work:
            __M_writer(u'    <a class="active_tab" href="')
            __M_writer(escape(url(controller='account', action='my_work')))
            __M_writer(u'"\n            data-intro=\'You will find all of your projects summarized on this tab\'\n            data-step=\'2\'>my work</a>\n    <a class="tab" href="')
            __M_writer(escape(url(controller='account', action='my_projects')))
            __M_writer(u'"\n            data-intro=\'On this tab you will find all the projects you are leading\'\n            data-step=\'3\'>my projects</a>\n')
        elif c.my_projects:
            __M_writer(u'    <a class="tab" href="')
            __M_writer(escape(url(controller='account', action='my_work')))
            __M_writer(u'"\n            data-intro=\'You will find all of your projects summarized on this tab\'\n            data-step=\'2\'>my work</a>\n    <a class="active_tab" href="')
            __M_writer(escape(url(controller='account', action='my_projects')))
            __M_writer(u'"\n            data-intro=\'On this tab you will find all the projects you are leading\'\n            data-step=\'3\'>my projects</a>\n')
        __M_writer(u'<div class="content">\n\n<br/> \n')
        if c.my_projects:
            __M_writer(u'\n')
            if len(c.leading_projects) > 0:
                __M_writer(u'        <h1>projects you\'re leading</h1>\n        <center>\n\n        <br/>\n        <table class="list_table">\n        \n')
                for i,review in enumerate(c.leading_projects):
                    __M_writer(u'        <tr class="')
                    __M_writer(escape('odd' if i%2 else 'even'))
                    __M_writer(u'">\n            <td><a href="')
                    __M_writer(escape(url(controller='review', action='show_review', id=review.id)))
                    __M_writer(u'">')
                    __M_writer(escape(review.name))
                    __M_writer(u'</td>           \n            <td class="inline-actions"><a href="')
                    __M_writer(escape(url(controller='review', action='admin', id=review.id)))
                    __M_writer(u'">admin \n                         <img src = "../../admin_sm.png"></a></td> \n            <td class="inline-actions">\n            <a href="#" onclick="javascript:    \n                      $(\'#export\').load(\'')
                    __M_writer(escape(url(controller="review", action="get_fields", review_id=review.id)))
                    __M_writer(u'\', \n                        function() {\n                            $(\'#export\').dialog(\'open\');\n                            $(\'#selectable\').selectable();\n                      });\n                      ">\n                      export<img src = "../../export_sm.png"></a></td>\n\n')
                    if c.projects_w_locked_priorities[review.id]:
                        __M_writer(u'                <td class="inline-actions"><a href="')
                        __M_writer(escape(url(controller='review', action='unlock_priorities', id=review.id)))
                        __M_writer(u'">unlock citations\n                            <img src = "../../unlock-icon.png"></a></td>\n')
                    else:
                        __M_writer(u'                <td class="inline-actions"><i>no citations locked</i></td>\n')
                    __M_writer(u'                    \n')
                    if c.statuses[review.id]:
                        __M_writer(u'                <td class="inline-actions"><a href="')
                        __M_writer(escape(url(controller='review', action='predictions_about_remaining_citations', id=review.id)))
                        __M_writer(u'">predictions\n                            <img src = "../../Robot-icon.png"></a></td>\n')
                    else:
                        __M_writer(u'                <td class="inline-actions"><i>no predictions yet</i></td>\n')
                    __M_writer(u'            \n            <td id="conflict_button_')
                    __M_writer(escape(review.id))
                    __M_writer(u'">loading...</td>\n            <script language="javascript">\n                $("#conflict_button_')
                    __M_writer(escape(review.id))
                    __M_writer(u'").load("/review/get_conflict_button_fragment/')
                    __M_writer(escape(review.id))
                    __M_writer(u'");\n            </script>\n            \n')
                    if c.do_we_have_a_maybe:
                        __M_writer(u'                <td class="inline-actions"><a href="')
                        __M_writer(escape(url(controller='review', action='review_maybes', id=review.id)))
                        __M_writer(u'">\n                    maybes<img src = "../../maybe_sm.png"></a></td>\n')
                    else:
                        __M_writer(u'                <td class="inline-actions"><i>no maybes yet</i></td>\n')
                    __M_writer(u'            \n            <td class="inline-actions">\n                <a href="#" onclick="javascript:jConfirm(\'are you sure you want to delete this review? all labels will be lost!\', \n                     \'delete review?\', function(r) {\n                        if(r) window.location = \'')
                    __M_writer(escape(url(controller='review', action='delete_review', id=review.id)))
                    __M_writer(u'\'; \n                   });">delete<img src = "../../delete.png"></a></td> \n        </tr>\n')
                __M_writer(u'        </table>\n        <br/><br/><br/>\n        </center>\n')
            __M_writer(u' \n')
            if len(c.participating_projects) > 0:
                __M_writer(u'        <h1>projects in which you\'re participating</h1>\n        <table class="list_table">\n')
                for i,review in enumerate(c.participating_projects):
                    __M_writer(u'        <tr class="')
                    __M_writer(escape('odd' if i%2 else 'even'))
                    __M_writer(u'">\n            <td><a href="')
                    __M_writer(escape(url(controller='review', action='show_review', id=review.id)))
                    __M_writer(u'">')
                    __M_writer(escape(review.name))
                    __M_writer(u'</td>    \n            <td class="inline-actions"><a href="')
                    __M_writer(escape(url(controller='review', action='review_labels', review_id=review.id)))
                    __M_writer(u'">review my labels</td>  \n            <td class="inline-actions"><a href="')
                    __M_writer(escape(url(controller='review', action='leave_review', id=review.id)))
                    __M_writer(u'" \n                           onclick="javascript:return confirm(\'are you sure you want to leave this review?\')">\n            leave review</a></td>      \n        </tr>\n')
                __M_writer(u'        </table>\n')
            else:
                if len(c.leading_projects) > 0:
                    __M_writer(u"            <h2>you're not participating in any projects yet (aside from those you're leading).</h2>\n")
                else:
                    __M_writer(u"            <h2>you're not participating in any projects yet.</h2>\n")
            __M_writer(u'    <br/>\n    \n    <br/><br/>\n\n    <center>\n     <div class="actions">\n\n')
            if len(c.leading_projects) > 1:
                __M_writer(u'        <a href="')
                __M_writer(escape(url(controller='account', action='show_merge_review_screen')))
                __M_writer(u'"><img src ="../../merge_sm.png">merge reviews ...</a>\n')
            __M_writer(u'    <a href="')
            __M_writer(escape(url(controller='review', action='create_new_review')))
            __M_writer(u'"><img src ="../../add.png">start a new project/review</a>\n    </center>    \n    </div>\n\n    \n')
        elif c.my_work:
            __M_writer(u'\n')
            if len(c.outstanding_assignments) > 0:
                __M_writer(u'        <h1>work you should be doing </h1>\n        <center>\n        <table class="list_table" align="center>>\n                <tr align="center">\n                <th width="25%">review</th><th >number to screen</th><th>screened so far</th><th width="20%">assigned</th><th width="10%">due</th><th width="30%">actions</th>\n                </tr>\n')
                for i, assignment in enumerate(c.outstanding_assignments):
                    __M_writer(u'                    <tr>\n                    <td><a href="')
                    __M_writer(escape(url(controller='review', action='show_review', id=assignment.project_id)))
                    __M_writer(u'">\n                            ')
                    __M_writer(escape(c.review_ids_to_names_d[assignment.project_id]))
                    __M_writer(u'</td>          \n')
                    if not assignment.assignment_type == "perpetual":
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.num_assigned))
                        __M_writer(u'</td>\n')
                    else:
                        __M_writer(u'                        <td>--</td>\n')
                    __M_writer(u'                    \n                    <td>')
                    __M_writer(escape(c.d_completion_status[assignment.id]))
                    __M_writer(u'</td>\n                    <td>')
                    __M_writer(escape(assignment.date_assigned.month))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.day))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.year))
                    __M_writer(u'</td>\n')
                    if not assignment.assignment_type == "perpetual" and assignment.date_due is not None:
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.date_due.month))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.day))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.year))
                        __M_writer(u'</td>\n')
                    else:
                        __M_writer(u'                        <td>--</td>\n')
                    __M_writer(u'                    <td class="inline-actions">\n                    <a href="')
                    __M_writer(escape(url(controller='review', action='screen', review_id=assignment.project_id, assignment_id=assignment.id)))
                    __M_writer(u'">\n                    screen <img src="../../arrow_right.png"></img></a>\n                    <a href="')
                    __M_writer(escape(url(controller='review', action='review_labels', review_id=assignment.project_id, assignment_id=assignment.id)))
                    __M_writer(u'">review labels <img src="../../arrow_right.png"></a>\n                    </td>\n                    </tr>\n')
                __M_writer(u'        </table>\n        </center>\n         <br/><br/>\n')
            else:
                __M_writer(u"        <h2>hurray, you've no outstanding assignments!</h2><br/><br/>\n")
            __M_writer(u'    \n')
            if len(c.finished_assignments) > 0:
                __M_writer(u'        <h1>assignments you\'ve completed</h1>\n        <center>\n        <table width=80% class="list_table" align="center>>\n                <tr align="center">\n<th width="25%">review</th><th >number to screen</th><th>screened so far</th><th width="20%">assigned</th><th width="10%">due</th><th width="30%">actions</th>\n                </tr>\n')
                for i,assignment in enumerate(c.finished_assignments):
                    __M_writer(u'                    <tr>\n                    <td><a href="')
                    __M_writer(escape(url(controller='review', action='show_review', id=assignment.project_id)))
                    __M_writer(u'">\n                            ')
                    __M_writer(escape(c.review_ids_to_names_d[assignment.project_id]))
                    __M_writer(u'</td>          \n')
                    if not assignment.assignment_type == "perpetual":
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.num_assigned))
                        __M_writer(u'</td>\n')
                    else:
                        __M_writer(u'                        <td>--</td>\n')
                    __M_writer(u'                    <td>')
                    __M_writer(escape(assignment.done_so_far))
                    __M_writer(u'</td>\n                    <td>')
                    __M_writer(escape(assignment.date_assigned.month))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.day))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.year))
                    __M_writer(u'</td>\n')
                    if not assignment.assignment_type == "perpetual" and assignment.date_due is not None:
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.date_due.month))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.day))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.year))
                        __M_writer(u'</td>\n')
                    else:
                        __M_writer(u'                        <td>--</td>\n')
                    __M_writer(u'                        <td class="inline-actions">\n                                      <a href="')
                    __M_writer(escape(url(controller='review', action='review_labels', review_id=assignment.project_id, assignment_id=assignment.id)))
                    __M_writer(u'">review labels <img src="../../arrow_right.png"></a>\n                        </td>\n                    </td>\n                    </tr>\n')
                __M_writer(u'        </table>\n        </center>\n')
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'home')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 32, "39": 33, "40": 33, "41": 33, "42": 36, "43": 36, "44": 39, "45": 40, "46": 40, "47": 40, "48": 43, "49": 43, "50": 47, "51": 50, "52": 51, "53": 52, "54": 53, "55": 59, "56": 60, "57": 60, "58": 60, "59": 61, "60": 61, "61": 61, "62": 61, "63": 62, "64": 62, "65": 66, "66": 66, "67": 74, "68": 75, "69": 75, "70": 75, "71": 77, "72": 78, "73": 80, "74": 81, "75": 82, "76": 82, "77": 82, "78": 84, "79": 85, "80": 87, "81": 88, "82": 88, "83": 90, "84": 90, "85": 90, "86": 90, "87": 93, "88": 94, "89": 94, "90": 94, "91": 96, "92": 97, "93": 99, "94": 103, "95": 103, "96": 107, "97": 111, "98": 112, "99": 113, "100": 115, "101": 116, "102": 116, "103": 116, "104": 117, "105": 117, "106": 117, "107": 117, "108": 118, "109": 118, "110": 119, "111": 119, "112": 124, "113": 125, "114": 126, "115": 127, "116": 128, "117": 129, "118": 132, "119": 139, "120": 140, "121": 140, "122": 140, "123": 142, "124": 142, "125": 142, "126": 147, "127": 148, "128": 149, "129": 150, "130": 156, "131": 157, "132": 158, "133": 158, "134": 159, "135": 159, "136": 160, "137": 161, "138": 161, "139": 161, "140": 162, "141": 163, "142": 165, "143": 166, "144": 166, "145": 167, "146": 167, "147": 167, "148": 167, "149": 167, "150": 167, "151": 168, "152": 169, "153": 169, "154": 169, "155": 169, "156": 169, "157": 169, "158": 169, "159": 170, "160": 171, "161": 173, "162": 174, "163": 174, "164": 176, "165": 176, "166": 180, "167": 183, "168": 184, "169": 186, "170": 187, "171": 188, "172": 194, "173": 195, "174": 196, "175": 196, "176": 197, "177": 197, "178": 198, "179": 199, "180": 199, "181": 199, "182": 200, "183": 201, "184": 203, "185": 203, "186": 203, "187": 204, "188": 204, "189": 204, "190": 204, "191": 204, "192": 204, "193": 205, "194": 206, "195": 206, "196": 206, "197": 206, "198": 206, "199": 206, "200": 206, "201": 207, "202": 208, "203": 210, "204": 211, "205": 211, "206": 216, "207": 220, "213": 2, "217": 2, "223": 217}, "uri": "/accounts/dashboard.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/accounts/dashboard.mako"}
__M_END_METADATA
"""
