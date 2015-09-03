# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438909704.207412
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/citation_fragment.mako'
_template_uri = '/citation_fragment.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['write_label']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def write_label(label):
            return render_write_label(context._locals(__M_locals),label)
        c = context.get('c', UNDEFINED)
        dir = context.get('dir', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<h2>')
        __M_writer(escape(c.cur_citation.marked_up_title))
        __M_writer(u'</h2>\n')
        if c.show_journal==True:
            __M_writer(u'    <i>Journal: ')
            __M_writer(escape(c.cur_citation.journal))
            __M_writer(u'</i><br><br>\n')
        __M_writer(u'\n')
        if c.show_authors==True:
            __M_writer(u'    Authors: ')
            __M_writer(escape(c.cur_citation.authors))
            __M_writer(u'<br><br>\n')
        __M_writer(u'\n')
        __M_writer(escape(c.cur_citation.marked_up_abstract))
        __M_writer(u'<br><br>\n\n')
        if c.show_keywords==True:
            __M_writer(u'    <b>keywords:</b> ')
            __M_writer(escape(c.cur_citation.keywords))
            __M_writer(u'<br><br>\n')
        __M_writer(u'\n<b>ID:</b> <span id="cur_citation_id" data-cur_citation_id="')
        __M_writer(escape(c.cur_citation.id))
        __M_writer(u'">')
        __M_writer(escape(c.cur_citation.id))
        __M_writer(u'</span><br><br>\n\n')
        __M_writer(u'\n\n')
        if c.cur_lbl is not None:
            if c.assignment_type == "conflict":
                for label in c.cur_lbl:
                    if "consensus_review" in dir(c) and c.consensus_review:
                        __M_writer(u'                a <b>consensus</b> label of ')
                        __M_writer(escape(write_label(label.label)))
                        __M_writer(u' was given for this citation on on ')
                        __M_writer(escape(label.label_last_updated))
                        __M_writer(u'<br>\n')
                    else:
                        __M_writer(u'                <b>')
                        __M_writer(escape(c.reviewer_ids_to_names_d[label.user_id]))
                        __M_writer(u'</b> labeled this citation as ')
                        __M_writer(escape(write_label(label.label)))
                        __M_writer(u' on ')
                        __M_writer(escape(label.label_last_updated))
                        __M_writer(u'<br>\n')
            else:
                __M_writer(u'        <center>you labeled this citation as ')
                __M_writer(escape(write_label(c.cur_lbl.label)))
                __M_writer(u' on ')
                __M_writer(escape(c.cur_lbl.label_last_updated))
                __M_writer(u'</center>\n')
        __M_writer(u'\n\n\n<script type="text/javascript">\n\nfunction populate_notes() {\n')
        if "notes" in dir(c) and c.notes is not None:
            __M_writer(u'        $("#pop_notes").val(\'')
            __M_writer(escape(c.notes.population))
            __M_writer(u'\');\n        $("textarea#general_notes").val(\'')
            __M_writer(escape(c.notes.general))
            __M_writer(u'\');\n        $("textarea#ic_notes").val(\'')
            __M_writer(escape(c.notes.ic))
            __M_writer(u'\');\n        $("textarea#outcome_notes").val(\'')
            __M_writer(escape(c.notes.outcome))
            __M_writer(u"');\n")
        else:
            __M_writer(u'        $("#pop_notes").val(\'\');\n        $("textarea#general_notes").val(\'\');\n        $("textarea#ic_notes").val(\'\');\n        $("textarea#outcome_notes").val(\'\');\n')
        __M_writer(u'};\n\nfunction setup_submit(){\n    $("#selectable").selectable();\n\n    $("#submit_btn").unbind();\n    $("#submit_btn").click(function() {\n        var tag_str = $("input#new_tag").val();\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n\n        // now add all selected tags to the study\n        var tags = $.map($(\'.ui-selected, this\'), function(element, i) {\n            return $(element).text();\n        });\n\n        // push new tag, too (if it\'s empty, we\'ll drop it server-side)\n        tags.push(tag_str);\n\n        $.post("')
        __M_writer(escape('/review/tag_citation/%s/' % (c.review_id)))
        __M_writer(u'" + cur_citation_id, {tags: tags}, function() {\n            $("#tags").fadeOut(\'slow\', function() {\n                $("#tags").load("/review/update_tags/" + cur_citation_id + "/')
        __M_writer(escape('%s/%s' % (c.tag_privacy, c.assignment_type)))
        __M_writer(u'", function() {\n                    $("#tags").fadeIn(\'slow\');\n                });\n            });\n\n            $("#dialog").load("')
        __M_writer(escape('/review/update_tag_types/%s/' % (c.review_id)))
        __M_writer(u'" + cur_citation_id);\n        });\n        $( "#dialog" ).dialog( "close" );\n    });\n\n    $("#save_notes_btn").unbind();\n    $("#save_notes_btn").click(function() {\n        var general_notes = $("#general_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var pop_notes =  $("#pop_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var ic_notes = $("#ic_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var outcome_notes = $("#outcome_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n\n')
        __M_writer(u'        $.post("/review/add_notes/" + cur_citation_id, {"general_notes": general_notes, "population_notes":pop_notes, "ic_notes":ic_notes, "outcome_notes":outcome_notes}, function() {\n            $("#notes-status").html("<font color=\'green\'>notes added.</font>");\n            $("#notes-dialog" ).dialog( "close" );\n            $("#notes-status").html("");\n        });\n    });\n\n    $("#tag_btn").unbind();\n    $("#tag_btn").click(function() {\n        $("#dialog" ).dialog( "open" );\n    });\n\n    $("#close_btn").unbind();\n    $("#close_btn").click(function (e) {\n        // I actually don\'t know where \'close_btn\' is defined...\n        // we close them both here.\n        $("#dialog" ).dialog( "close" );\n        $("#notes-dialog" ).dialog( "close" );\n    });\n\n    $("#notes_btn").unbind();\n    $("#notes_btn").click(function() {\n        $("#notes-dialog" ).dialog("open");\n    });\n    $("#new_tag").val(\' \');\n};\n\nfunction setup_js(){\n    // unbind all attached events\n    $("#accept").unbind();\n    $("#maybe").unbind();\n    $("#reject").unbind();\n    $("#pos_lbl_term").unbind();\n    $("#double_pos_lbl_term").unbind();\n    $("#neg_lbl_term").unbind();\n    $("#double_neg_lbl_term").unbind();\n    $("#submit_btn").unbind();\n    $("#close_btn").unbind();\n    $("#tag_btn").unbind();\n\n')
        __M_writer(u'\n    $("#tags").load("')
        __M_writer(escape('/review/update_tags/%s/%s/%s' % (c.cur_citation.id, c.tag_privacy, c.assignment_type)))
        __M_writer(u'");\n\n    // reset the timer\n    reset_timer();\n\n    function markup_current() {\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n        var next_citation_id = $(\'#hidden_div.content span#cur_citation_id\').text();\n        // reload the current citation, with markup\n')
        __M_writer(u'        $("#wait").text("marking up the current citation..")\n        $("#citation").fadeOut(\'slow\', function() {\n            $("#citation").load("')
        __M_writer(escape('/markup/%s/%s/' % (c.review_id, c.assignment_id)))
        __M_writer(u'" + cur_citation_id, function() {\n                $("#citation").fadeIn(\'slow\');\n                $("#wait").text("");\n            });\n        });\n')
        __M_writer(u'        $("#citation").fadeOut(\'fast\', function() {\n            $("#hidden_div").load("')
        __M_writer(escape('/markup/%s/%s/' % (c.review_id, c.assignment_id)))
        __M_writer(u'" + next_citation_id, function() {\n                $("#citation").fadeIn(\'slow\');\n                $("#wait").text("");\n            });\n        });\n    };\n\n    function label_cur_citation(lbl_str){\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n\n        $("#citation").fadeOut(\'fast\', function() {\n            if (!(we_are_reviewing_a_label()) && is_perpetual_assignment()){\n                // try to load the next citation\n                // this call will in turn call get_next_citation\n                // once loading is complete\n                load_next_citation();\n            };\n            $.post("')
        __M_writer(escape('/label/%s/%s/' % (c.review_id, c.assignment_id)))
        __M_writer(u'" + cur_citation_id + "/" + seconds + "/" + lbl_str, function(data) {\n                if (we_are_reviewing_a_label()){\n                    // in the case that we are re-labeling a citation,\n                    // this the label method will return the citation fragment.\n                    $(\'#citation\').html(data);\n                    $(\'#citation\').fadeIn();\n                    setup_js();\n                    still_loading = false;\n                }\n                else if (!(is_perpetual_assignment())) {\n                    load_next_citation();\n                }\n                else {\n')
        __M_writer(u'                    $(\'#progress\').html(data);\n                };\n            });\n        });\n        $("#general_notes").val("");\n        $("#pop_notes").val("");\n        $("#ic_notes").val("");\n        $("#outcome_notes").val("");\n    };\n\n    $("#accept").click(function() {\n        label_cur_citation("1");\n    });\n\n    $("#maybe").click(function() {\n        label_cur_citation("0");\n    });\n\n    $("#reject").click(function() {\n        label_cur_citation("-1");\n    });\n\n    $("#pos_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val()\n        if (term_str != ""){\n            $.post("')
        __M_writer(escape('/label_term/%s/1' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'green\'>" + term_str + "</font> as being indicative of relevance.")\n            $("#label_msg").fadeIn(2000)\n            $("input#term").val("")\n            $("#label_msg").fadeOut(3000)\n            markup_current();\n        };\n    });\n\n    $("#double_pos_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val()\n        if (term_str != ""){\n            $.post("')
        __M_writer(escape('/label_term/%s/2' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'green\'>" + term_str + "</font> as being <bold>strongly</bold> indicative of relevance.")\n            $("#label_msg").fadeIn(2000)\n            $("input#term").val("")\n            $("#label_msg").fadeOut(3000)\n            markup_current();\n        };\n    });\n\n\n    $("#neg_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val()\n        if (term_str != ""){\n            $.post("')
        __M_writer(escape('/label_term/%s/-1' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'red\'>" + term_str + "</font> as being indicative of <i>ir</i>relevance.")\n            $("#label_msg").fadeIn(2000)\n            $("input#term").val("")\n            $("#label_msg").fadeOut(3000)\n            markup_current();\n        }\n    });\n\n    $("#double_neg_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val()\n        if (term_str != ""){\n            $.post("')
        __M_writer(escape('/label_term/%s/-2' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'red\'>" + term_str + "</font> as being <bold>strongly</bold> indicative of <i>ir</i>relevance.");\n            $("#label_msg").fadeIn(2000);\n            $("input#term").val("");\n            $("#label_msg").fadeOut(3000);\n            markup_current();\n        }\n    });\n\n')
        if 'assignment' in dir(c):
            if c.assignment.num_assigned and c.assignment.num_assigned > 0:
                __M_writer(u'            $("#progress").html("you\'ve screened <b>')
                __M_writer(escape(c.assignment.done_so_far))
                __M_writer(u'</b> out of <b>')
                __M_writer(escape(c.assignment.num_assigned))
                __M_writer(u'</b> so far (nice going!)");\n')
            else:
                __M_writer(u'            $("#progress").html("you\'ve screened <b>')
                __M_writer(escape(c.assignment.done_so_far))
                __M_writer(u'</b> abstracts thus far (keep it up!)");\n')
        else:
            __M_writer(u'        $("#progress").html("");\n')
        __M_writer(u'};\n\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_write_label(context,label):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        if label == 1:
            __M_writer(u'        <b><font color=\'green\'>"relevant"</font></b>\n')
        elif label == 0:
            __M_writer(u'        <b><font color=\'light green\'>"maybe" (?)</font></b>\n')
        else:
            __M_writer(u'        <b><font color=\'red\'>"irrelevant"</font></b>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "25": 1, "26": 1, "27": 1, "28": 2, "29": 3, "30": 3, "31": 3, "32": 5, "33": 6, "34": 7, "35": 7, "36": 7, "37": 9, "38": 10, "39": 10, "40": 12, "41": 13, "42": 13, "43": 13, "44": 15, "45": 16, "46": 16, "47": 16, "48": 16, "49": 26, "50": 28, "51": 29, "52": 30, "53": 31, "54": 32, "55": 32, "56": 32, "57": 32, "58": 32, "59": 33, "60": 34, "61": 34, "62": 34, "63": 34, "64": 34, "65": 34, "66": 34, "67": 37, "68": 38, "69": 38, "70": 38, "71": 38, "72": 38, "73": 41, "74": 47, "75": 48, "76": 48, "77": 48, "78": 49, "79": 49, "80": 50, "81": 50, "82": 51, "83": 51, "84": 52, "85": 53, "86": 58, "87": 76, "88": 76, "89": 78, "90": 78, "91": 83, "92": 83, "93": 97, "94": 142, "95": 143, "96": 143, "97": 153, "98": 155, "99": 155, "100": 161, "101": 162, "102": 162, "103": 179, "104": 179, "105": 193, "106": 219, "107": 219, "108": 232, "109": 232, "110": 246, "111": 246, "112": 259, "113": 259, "114": 268, "115": 269, "116": 270, "117": 270, "118": 270, "119": 270, "120": 270, "121": 271, "122": 272, "123": 272, "124": 272, "125": 274, "126": 275, "127": 277, "133": 18, "137": 18, "138": 19, "139": 20, "140": 21, "141": 22, "142": 23, "143": 24, "149": 143}, "uri": "/citation_fragment.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/citation_fragment.mako"}
__M_END_METADATA
"""
