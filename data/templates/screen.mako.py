# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438909704.078237
_enable_loop = True
_template_filename = '/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/screen.mako'
_template_uri = '/screen.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['write_label', 'title']


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
    return runtime._inherit_from(context, u'site.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def write_label(label):
            return render_write_label(context._locals(__M_locals),label)
        c = context.get('c', UNDEFINED)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        dir = context.get('dir', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n\n<script type="text/javascript">\n    var seconds = 1;\n    setTimeout(update_timer, 1000);\n\n    function reset_timer() {\n        seconds = 1; // start at one\n        setTimeout(update_timer, 1000);\n    }\n\n    function update_timer() {\n        seconds +=1;\n        setTimeout(update_timer, 1000);\n    }\n</script>\n\n\n<div id="dialog">\n    <form>\n        <center>\n            new tag: <input type="text" id="new_tag" name="new_tag" /> </input><br>\n        </center><br>\n\n        <ul id="selectable" class="ui-selectable">\n')
        for tag in c.tag_types:
            if tag in c.tags:
                __M_writer(u'                    <li class="ui-selected">')
                __M_writer(escape(tag))
                __M_writer(u'</li>\n')
            else:
                __M_writer(u'                    <li>')
                __M_writer(escape(tag))
                __M_writer(u'</li>\n')
        __M_writer(u'        </ul>\n\n        <div class="actions" style="text-align: right;">\n            <input id="submit_btn" type="button" value="tag" />\n        </div>\n    </form>\n</div>\n\n\n<div id="notes-dialog">\n    <form>\n        <b>general notes</b><br>\n        <textarea id="general_notes" name="general_notes" rows="4" cols="40" /></textarea><br><br>\n\n        <b>population notes</b><br>\n        <textarea id="pop_notes" name="pop_notes" rows="1" cols="40" /></textarea><br><br>\n\n        <b>intervention/comparator notes</b><br>\n        <textarea id="ic_notes" name="ic_notes" rows="1" cols="40" /></textarea><br><br>\n\n        <b>outcome notes</b><br>\n        <textarea id="outcome_notes" name="outcome_notes" rows="1" cols="40" /> </textarea><br><br>\n\n        <div id="notes-status"></div>\n\n        <div class="actions" style="text-align: right;">\n            <input id="save_notes_btn" type="button" value="save notes" />\n        </div>\n    </form>\n</div>\n\n\n<div class="actions">\n')
        if c.cur_lbl is not None and c.assignment_type != "conflict":
            if c.assignment_id is not None:
                __M_writer(u'            <a href="')
                __M_writer(escape(url(controller='review', action='screen', review_id=c.review_id, assignment_id=c.assignment_id)))
                __M_writer(u'">back to screening <img src="/arrow_right.png"></img></a>\n            <a href="')
                __M_writer(escape(url(controller='review', action='review_labels', review_id=c.review_id, assignment_id=c.assignment_id)))
                __M_writer(u'">back to the list of labeled citations <img src="/arrow_right.png"></img></a>\n')
        else:
            __M_writer(u'        <a href="')
            __M_writer(escape(url(controller='review', action='review_labels', review_id=c.review_id, assignment_id=c.assignment_id)))
            __M_writer(u'">review labels</a>\n        <a href="')
            __M_writer(escape(url(controller='review', action='review_terms', id=c.review_id, assignment_id=c.assignment_id)))
            __M_writer(u'">review terms</a>\n')
        __M_writer(u'</div>\n\n\n<div class="container">\n    <div id="tags_container" class="sidebar">\n        <h2>tags &amp; notes</h2><br>\n        <center>\n            <div id="tags" class="tags">\n                <ul>\n')
        if len(c.tags) > 0:
            for i,tag in enumerate(c.tags):
                __M_writer(u'                        <li class=')
                __M_writer(escape("tag%s"%(i+1)))
                __M_writer(u'><a href="#">')
                __M_writer(escape(tag))
                __M_writer(u'</a></li><br>\n')
            __M_writer(u'                </ul>\n')
        else:
            __M_writer(u'                    (no tags yet.)\n')
        __M_writer(u'            </div><br>\n            <input type="button" style="width: 120px" id="tag_btn" value="tag study..."/><br><br>\n            <input type="button" style="width: 120px" id="edit_tags_btn" value="edit tags..." onclick="parent.location=\'/review/edit_tags/')
        __M_writer(escape(c.review_id))
        __M_writer(u'/')
        __M_writer(escape(c.assignment_id))
        __M_writer(u'\'"><br><br>\n            <input type="button" style="width: 120px" id="notes_btn" value="notes..."/><br><br>\n        </center>\n    </div>\n\n    <div id="citation-holder" style=\'float: right; width: 85%;\'>\n        <div id="citation" class="content">\n            <h2>')
        __M_writer(escape(c.cur_citation.marked_up_title))
        __M_writer(u'</h2>\n')
        if c.show_journal==True:
            __M_writer(u'                <i>Journal: ')
            __M_writer(escape(c.cur_citation.journal))
            __M_writer(u'</i><br><br>\n')
        __M_writer(u'\n')
        if c.show_authors==True:
            __M_writer(u'                Authors: ')
            __M_writer(escape(c.cur_citation.authors))
            __M_writer(u'<br><br>\n')
        __M_writer(u'\n            ')
        __M_writer(escape(c.cur_citation.marked_up_abstract))
        __M_writer(u'<br><br>\n\n')
        if c.show_keywords==True:
            __M_writer(u'                <b>keywords:</b> ')
            __M_writer(escape(c.cur_citation.keywords))
            __M_writer(u'<br><br>\n')
        __M_writer(u'\n            <b>ID:</b> <span id="cur_citation_id" data-cur_citation_id="')
        __M_writer(escape(c.cur_citation.id))
        __M_writer(u'">')
        __M_writer(escape(c.cur_citation.id))
        __M_writer(u'</span><br><br>\n\n            ')
        __M_writer(u'\n\n')
        if c.cur_lbl is not None:
            if c.assignment_type == "conflict":
                for label in c.cur_lbl:
                    if "consensus_review" in dir(c) and c.consensus_review:
                        __M_writer(u'                            a <b>consensus</b> label of ')
                        __M_writer(escape(write_label(label.label)))
                        __M_writer(u' was given for this citation on on ')
                        __M_writer(escape(label.label_last_updated))
                        __M_writer(u'<br>\n')
                    else:
                        __M_writer(u'                            <b>')
                        __M_writer(escape(c.reviewer_ids_to_names_d[label.user_id]))
                        __M_writer(u'</b> labeled this citation as ')
                        __M_writer(escape(write_label(label.label)))
                        __M_writer(u' on ')
                        __M_writer(escape(label.label_last_updated))
                        __M_writer(u'<br>\n')
            else:
                __M_writer(u'                    <center>you labeled this citation as ')
                __M_writer(escape(write_label(c.cur_lbl.label)))
                __M_writer(u' on ')
                __M_writer(escape(c.cur_lbl.label_last_updated))
                __M_writer(u'</center>\n')
        __M_writer(u'        </div> <!-- <div id="citation" class="content"> -->\n\n        <div id="hidden_div" class="content"></div>\n\n        <center><div id="wait"></div></center><br><br>\n\n        <center>\n            <div id="progress">\n')
        if 'assignment' in dir(c):
            if c.assignment.num_assigned and c.assignment.num_assigned > 0:
                __M_writer(u"                        you've screened <b>")
                __M_writer(escape(c.assignment.done_so_far))
                __M_writer(u'</b> out of <b>')
                __M_writer(escape(c.assignment.num_assigned))
                __M_writer(u'</b> so far (nice going!)\n')
            else:
                __M_writer(u"                        you've screened <b>")
                __M_writer(escape(c.assignment.done_so_far))
                __M_writer(u'</b> abstracts thus far (keep it up!)\n')
        __M_writer(u'            </div>\n        </center>\n\n        <center>\n            <br clear="all"/>\n            <div id = "buttons" >\n                <a href="#" id="accept"><img src = "/accept.png"/></a>\n                <a href="#" id="maybe"><img src = "/maybe.png"/></a>\n                <a href="#" id="reject"><img src = "/reject.png"/></a>\n            </div>\n            <div id="label_terms" class="summary_heading">\n                <table>\n                    <tr>\n                        <td><label>term: ')
        __M_writer(escape(h.text('term')))
        __M_writer(u'</label></td>\n                        <td width="10"></td>\n                        <td><a href="#" id="pos_lbl_term"><img src = "/thumbs_up.png" border="2" alt="indicative of relevance"></a></td>\n                        <td><a href="#" id="double_pos_lbl_term"><img src = "/two_thumbs_up.png" border="2" alt="strongly indicative of relevance"></a></td>\n                        <td width="10"></td>\n                        <td><a href="#" id="neg_lbl_term"><img src = "/thumbs_down.png"/ border="2" alt="indicative of irrelevance" ></a></td>\n                        <td><a href="#" id="double_neg_lbl_term"><img src = "/two_thumbs_down.png"/ border="2" alt="strongly indicative of irrelevance"></a></td>\n                    </tr>\n                </table>\n            </div>\n            <div id="label_msg"></div>\n        </center>\n    </div>\n</div>\n\n\n<script type="text/javascript">\n\nvar still_loading = false;\nvar waiting_for_citation = false;\n\nfunction get_next_citation() {\n    still_loading = true;\n    $(\'#hidden_div\').load( "')
        __M_writer(escape('/next_citation/%s/%s' % (c.review_id, c.assignment_id)))
        __M_writer(u'", function() {\n        still_loading = false;\n        // were we waiting for this guy? if so, load\n        // him in now\n        if (waiting_for_citation) {\n            load_next_citation();\n        };\n    });\n};\n\nfunction load_next_citation() {\n    // pull in the next citation from the hidden_div iff\n    // it has finished downloading. otherwise hide buttons,\n    // show waiting screen and flip \'waiting_for_citation\'\n    // boolean to true\n    if (still_loading) {\n        $("#wait").text("hold on to your horses..");\n        $(\'#buttons\').hide();\n        waiting_for_citation = true;\n    } else {\n        // then the next citation has been downloaded\n        // into the hidden_div\n        $(\'#citation\').html( $(\'#hidden_div\').html() );\n\n        // this is the key logic piece; we the setup_js method\n        // is defined with respect to the currently hidden\n        // citation that we just loaded into the #citation div\n        // hence when it is called it will attach calls to the\n        // buttons that label the (now currently) displayed\n        // citation that we fadein in the next line.\n        setup_js();\n\n        $(\'#citation\').fadeIn();\n        $("#wait").text("");\n        $(\'#buttons\').show();\n        waiting_for_citation = false;\n\n        // once the citation\n        get_next_citation();\n    };\n};\n\nfunction we_are_reviewing_a_label() {\n    return "')
        __M_writer(escape('assignment' not in dir(c)))
        __M_writer(u'" == "True";\n};\n\nfunction is_perpetual_assignment() {\n')
        if not 'assignment' in dir(c):
            __M_writer(u'        return false;\n')
        else:
            __M_writer(u'        return "')
            __M_writer(escape(c.assignment.assignment_type))
            __M_writer(u'" == "perpetual";\n')
        __M_writer(u'};\n\nfunction populate_notes() {\n')
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
        __M_writer(u'};\n\nfunction setup_submit() {\n    $("#selectable").selectable();\n\n    $("#submit_btn").unbind();\n    $("#submit_btn").click(function() {\n        var tag_str = $("input#new_tag").val();\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n\n        // now add all selected tags to the study\n        var tags = $.map($(\'.ui-selected, this\'), function(element, i) {\n            return $(element).text();\n        });\n\n        // push new tag, too (if it\'s empty, we\'ll drop it server-side)\n        tags.push(tag_str);\n\n        $.post("')
        __M_writer(escape('/review/tag_citation/%s/' % (c.review_id)))
        __M_writer(u'" + cur_citation_id, {tags: tags}, function() {\n            $("#tags").fadeOut(\'slow\', function() {\n                $("#tags").load("/review/update_tags/" + cur_citation_id + "/')
        __M_writer(escape('%s/%s' % (c.tag_privacy, c.assignment_type)))
        __M_writer(u'", function() {\n                    $("#tags").fadeIn(\'slow\');\n                });\n            });\n            $("#dialog").load("')
        __M_writer(escape('/review/update_tag_types/%s/' % (c.review_id)))
        __M_writer(u'" + cur_citation_id);\n        });\n        $( "#dialog" ).dialog( "close" );\n    });\n\n    $("#save_notes_btn").unbind();\n    $("#save_notes_btn").click(function() {\n        var general_notes = $("#general_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var pop_notes =  $("#pop_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var ic_notes = $("#ic_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var outcome_notes = $("#outcome_notes").val().replace(/\\n\\r?/g, \'\\\\n\');\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n\n')
        __M_writer(u'        $.post("/review/add_notes/" + cur_citation_id, {"general_notes": general_notes, "population_notes":pop_notes, "ic_notes":ic_notes, "outcome_notes":outcome_notes}, function() {\n            $("#notes-status").html("<font color=\'green\'>notes added.</font>");\n            $("#notes-dialog" ).dialog( "close" );\n            $("#notes-status").html("");\n        });\n    });\n\n    $("#tag_btn").unbind();\n    $("#tag_btn").click(function() {\n        $("#dialog" ).dialog( "open" );\n    });\n\n    $("#close_btn").unbind();\n    $("#close_btn").click(function(e) {\n        // I actually don\'t know where \'close_btn\' is defined...\n        // we close them both here.\n        $("#dialog" ).dialog( "close" );\n        $("#notes-dialog" ).dialog( "close" );\n    });\n\n    $("#notes_btn").unbind();\n    $("#notes_btn").click(function() {\n        $("#notes-dialog" ).dialog("open");\n    });\n};\n\nfunction setup_js() {\n\n    $( "#dialog" ).dialog({\n        height: 250,\n        modal: true,\n        autoOpen: false,\n        show: "blind",\n    });\n\n    $( "#notes-dialog" ).dialog({\n        height: 500,\n        width: 400,\n        modal: true,\n        autoOpen: false,\n        position: [0,0],\n        show: "blind",\n        hide: {effect: "fadeOut", duration:2000}\n    });\n\n    function markup_current() {\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n        var next_citation_id = $(\'#hidden_div.content span#cur_citation_id\').text();\n        // reload the current citation, with markup\n        $("#wait").text("marking up the current citation..")\n        $("#citation").fadeOut(\'slow\', function() {\n            $("#citation").load("')
        __M_writer(escape('/markup/%s/%s/' % (c.review_id, c.assignment_id)))
        __M_writer(u'" + cur_citation_id, function() {\n                $("#citation").fadeIn(\'slow\');\n                $("#wait").text("");\n            });\n        });\n        $("#citation").fadeOut(\'fast\', function() {\n            $("#hidden_div").load("')
        __M_writer(escape('/markup/%s/%s/' % (c.review_id, c.assignment_id)))
        __M_writer(u'" + next_citation_id, function() {\n                $("#citation").fadeIn(\'slow\');\n                $("#wait").text("");\n            });\n        });\n    };\n\n    function label_cur_citation(lbl_str) {\n        var cur_citation_id = $(\'#citation.content span#cur_citation_id\').text();\n\n        $("#citation").fadeOut(\'fast\', function() {\n            if (!(we_are_reviewing_a_label()) && is_perpetual_assignment()) {\n                // try to load the next citation\n                // this call will in turn call get_next_citation\n                // once loading is complete\n                load_next_citation();\n            };\n            $.post("')
        __M_writer(escape('/label/%s/%s/' % (c.review_id, c.assignment_id)))
        __M_writer(u'" + cur_citation_id + "/" + seconds + "/" + lbl_str, function(data) {\n                if (we_are_reviewing_a_label()) {\n                    // in the case that we are re-labeling a citation,\n                    // this the label method will return the citation fragment.\n                    $(\'#citation\').html(data);\n                    $(\'#citation\').fadeIn();\n                    setup_js();\n                    still_loading = false;\n                } else if (!(is_perpetual_assignment())) {\n                    load_next_citation();\n                } else {\n                    $(\'#progress\').html(data);\n                };\n            });\n        });\n        $("#general_notes").val("");\n        $("#pop_notes").val("");\n        $("#ic_notes").val("");\n        $("#outcome_notes").val("");\n    };\n\n    $("#accept").click(function() {\n        label_cur_citation("1");\n    });\n\n    $("#maybe").click(function() {\n        label_cur_citation("0");\n    });\n\n    $("#reject").click(function() {\n        label_cur_citation("-1");\n    });\n\n    $("#pos_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val();\n        if (term_str != "") {\n            $.post("')
        __M_writer(escape('/label_term/%s/1' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'green\'>" + term_str + "</font> as being indicative of relevance.");\n            $("#label_msg").fadeIn(2000);\n            $("input#term").val("");\n            $("#label_msg").fadeOut(3000);\n            markup_current();\n        };\n    });\n\n    $("#double_pos_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val();\n        if (term_str != "") {\n            $.post("')
        __M_writer(escape('/label_term/%s/2' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'green\'>" + term_str + "</font> as being <bold>strongly</bold> indicative of relevance.");\n            $("#label_msg").fadeIn(2000);\n            $("input#term").val("");\n            $("#label_msg").fadeOut(3000);\n            markup_current();\n        };\n    });\n\n    $("#neg_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val()\n        if (term_str != "") {\n            $.post("')
        __M_writer(escape('/label_term/%s/-1' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'red\'>" + term_str + "</font> as being indicative of <i>ir</i>relevance.");\n            $("#label_msg").fadeIn(2000);\n            $("input#term").val("");\n            $("#label_msg").fadeOut(3000);\n            markup_current();\n        };\n    });\n\n    $("#double_neg_lbl_term").click(function() {\n        // call out to the controller to label the term\n        var term_str = $("input#term").val()\n        if (term_str != "") {\n            $.post("')
        __M_writer(escape('/label_term/%s/-2' % c.review_id))
        __M_writer(u'", {term: term_str});\n            $("#label_msg").html("ok. labeled <font color=\'red\'>" + term_str + "</font> as being <bold>strongly</bold> indicative of <i>ir</i>relevance.");\n            $("#label_msg").fadeIn(2000);\n            $("input#term").val("");\n            $("#label_msg").fadeOut(3000);\n            markup_current();\n        };\n    });\n\n    populate_notes();\n    setup_submit();\n};\n\n$(document).ready(function() {\n    setup_js();\n    // we don\'t queue the next citation if we\'re reviewing\n    // labels!\n    if (!(we_are_reviewing_a_label())) {\n        get_next_citation(); // fetch the *next* citation\n    }\n    $("#hidden_div").hide();\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_write_label(context,label):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        if label == 1:
            __M_writer(u'                    <b><font color=\'green\'>"relevant"</font></b>\n')
        elif label == 0:
            __M_writer(u'                    <b><font color=\'light green\'>"maybe" (?)</font></b>\n')
        else:
            __M_writer(u'                    <b><font color=\'red\'>"irrelevant"</font></b>\n')
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'screen')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "40": 1, "41": 2, "42": 28, "43": 29, "44": 30, "45": 30, "46": 30, "47": 31, "48": 32, "49": 32, "50": 32, "51": 35, "52": 68, "53": 69, "54": 70, "55": 70, "56": 70, "57": 71, "58": 71, "59": 73, "60": 74, "61": 74, "62": 74, "63": 75, "64": 75, "65": 77, "66": 86, "67": 87, "68": 88, "69": 88, "70": 88, "71": 88, "72": 88, "73": 90, "74": 91, "75": 92, "76": 94, "77": 96, "78": 96, "79": 96, "80": 96, "81": 103, "82": 103, "83": 104, "84": 105, "85": 105, "86": 105, "87": 107, "88": 108, "89": 109, "90": 109, "91": 109, "92": 111, "93": 112, "94": 112, "95": 114, "96": 115, "97": 115, "98": 115, "99": 117, "100": 118, "101": 118, "102": 118, "103": 118, "104": 128, "105": 130, "106": 131, "107": 132, "108": 133, "109": 134, "110": 134, "111": 134, "112": 134, "113": 134, "114": 135, "115": 136, "116": 136, "117": 136, "118": 136, "119": 136, "120": 136, "121": 136, "122": 139, "123": 140, "124": 140, "125": 140, "126": 140, "127": 140, "128": 143, "129": 151, "130": 152, "131": 153, "132": 153, "133": 153, "134": 153, "135": 153, "136": 154, "137": 155, "138": 155, "139": 155, "140": 158, "141": 171, "142": 171, "143": 194, "144": 194, "145": 237, "146": 237, "147": 241, "148": 242, "149": 243, "150": 244, "151": 244, "152": 244, "153": 246, "154": 249, "155": 250, "156": 250, "157": 250, "158": 251, "159": 251, "160": 252, "161": 252, "162": 253, "163": 253, "164": 254, "165": 255, "166": 260, "167": 278, "168": 278, "169": 280, "170": 280, "171": 284, "172": 284, "173": 298, "174": 349, "175": 349, "176": 355, "177": 355, "178": 372, "179": 372, "180": 409, "181": 409, "182": 422, "183": 422, "184": 435, "185": 435, "186": 448, "187": 448, "193": 120, "197": 120, "198": 121, "199": 122, "200": 123, "201": 124, "202": 125, "203": 126, "204": 128, "210": 2, "214": 2, "220": 214}, "uri": "/screen.mako", "filename": "/Users/mq20155490/Desktop/CEL/abstrackr_test/abstrackr/templates/screen.mako"}
__M_END_METADATA
"""
