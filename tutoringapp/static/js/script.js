function initMatchDragDrop() {
    $('.tutor-cand, .tutee-cand').draggable({
        helper: function(event) {
                    return $(event.target).parent().clone();
                }
    });

    $('#match-box').droppable({
        accept: '.tutor-cand, .tutee-cand',
        tolerance: 'pointer',
        drop: function(event, ui) {
            if(ui.helper.hasClass('tutee-cand')) {
                which = "tutee";
            } else if(ui.helper.hasClass('tutor-cand')) {
                which = "tutor";
            }
            $('#'+which+'-selected').html('<table>'+ui.helper.html()+'</table>');
            $('#'+which+'-selected').attr('rel',ui.helper.attr('rel'));
        }
    });
}

function clearMatchBox() {
    $('div.tutor-cand[rel='+tutor_id+']').slideUp();
    $('div.tutee-cand[rel='+tutee_id+']').slideUp();
    $('#tutor-selected').html('');
    $('#tutor-selected').attr('rel','');
    $('#tutee-selected').html('');
    $('#tutee-selected').attr('rel','');
    $('#match-note').val('');
}

function matchEditHandlers(base_url, reloadUrl) {
    noteSlideHandler();
    $('table.data tbody tr td').dblclick(function() {
        var dialog = $('<div style="display:none" title="Edit Match"></div>').
        appendTo('body');
        var match_id = $(this).parent().attr('id');
        var edit_url = base_url+""+match_id+"/";
        dialog.load(edit_url, function (responseText, textStatus, XMLHttpRequest) {
            dialog.dialog({
                modal: true,
                width: 800,
                close: function(event, ui) {
                    dialog.remove();
                    dataTable.fnReloadAjax(reloadUrl);
                    $('.ui-state-active').prev().trigger('click');
                }
            });
        });
        return false;
    });
}

function responseDeleteHandlers() {
    $('.response-delete').click(function(event) {
        event.preventDefault();
        var url = $(this).attr('href');
        var conf = confirm("Are you sure you want to delete this response?");
        var resp = $(this).closest('.response');
        if (conf) {
            $.ajax({
                type: "DELETE",
                url: url,
                success: function(data) {
                    resp.slideUp();
                }
            });
        }
        return false;
    });
}

function tutorEditHandlers(base_url) {
    noteSlideHandler();
    $('table.data tbody tr td').dblclick(function() {
        var dialog = $('<div style="display:none" title="Edit Tutor"></div>').
            appendTo('body');
        var tutor_id = $(this).parent().attr('id');
        var edit_url = base_url+""+tutor_id+"/";
        dialog.load(edit_url, function() {
            dialog.dialog({
                modal: true,
                width: 800,
                close: function(event, ui) {
                    dialog.remove();
                    $('.ui-state-active').prev().trigger('click');
                }
            });
        });
        return false;
    });
}

function tuteeEditHandlers(base_url) {
    noteSlideHandler();
    $('table.data tbody tr td').dblclick(function() {
        var dialog = $('<div style="display:none" title="Edit Tutee"></div>').
            appendTo('body');
        var tutee_id = $(this).parent().attr('id');
        var edit_url = base_url+""+tutee_id+"/";
        console.log(edit_url);
        dialog.load(edit_url, function() {
            dialog.dialog({
                modal: true,
                width: 800,
                close: function(event, ui) {
                    dialog.remove();
                    $('.ui-state-active').prev().trigger('click');
                }
            });
        });
        return false;
    });
}

function notificationNextHandler() {
  $('.notification-links a').click(function(event) {
      event.preventDefault();
      var link = $(this).attr('href');
      $("#notifications-list").load(link);
  });
}

function noteSlideHandler() {
    $('.data tr td:last-child').each(function(index, elem) {
        $(elem).attr('rel', $(elem).height());
    })
    $('.data tr td:last-child').click(function() {
        var temp = $(this).height();
        $(this).animate({height: $(this).attr('rel')}, 600);
        $(this).height($(this).attr('rel'));
        $(this).attr('rel',temp);
    });
    $('.data tr td:last-child').height('30');
}

function getResponseInit() {
    var form = $('#get-response');
    form.submit(function(event) {
        event.preventDefault();
        var dataStr = form.serialize();
        var the_url = form.attr('action');
        $.get(the_url, dataStr, function(data) {
            $('#response-div').html(data);
        });
    });
}

function responseAutocompleteInit() {
    $.each($('.resp-autocomplete'), function(i, elem) {
        var the_url = $(elem).attr('rel')
        $.getJSON(the_url, function(data) {
            $(elem).autocomplete({
                source: data,
                minLength: 2,
                delay: 0,
                select: function(e, v) {
                           $(elem).val(v.item.label);
                           return false;
                       },
                focus: function(e, v) {
                           $(elem).val(v.item.label);
                           $(elem).next().val(v.item.value);
                           return false;
                       },
            });
        });
    });
}

/* Datatables plugin */
$.fn.dataTableExt.oApi.fnReloadAjax = function ( oSettings, sNewSource, fnCallback, bStandingRedraw )
{
    if ( typeof sNewSource != 'undefined' && sNewSource != null )
    {
        oSettings.sAjaxSource = sNewSource;
    }
    this.oApi._fnProcessingDisplay( oSettings, true );
    var that = this;
    var iStart = oSettings._iDisplayStart;
     
    oSettings.fnServerData( oSettings.sAjaxSource, [], function(json) {
        /* Clear the old information from the table */
        that.oApi._fnClearTable( oSettings );
         
        /* Got the data - add it to the table */
        var aData =  (oSettings.sAjaxDataProp !== "") ?
            that.oApi._fnGetObjectDataFn( oSettings.sAjaxDataProp )( json ) : json;
         
        for ( var i=0 ; i<aData.length ; i++ )
        {
            that.oApi._fnAddData( oSettings, aData[i] );
        }
         
        oSettings.aiDisplay = oSettings.aiDisplayMaster.slice();
        that.fnDraw();
         
        if ( typeof bStandingRedraw != 'undefined' && bStandingRedraw === true )
        {
            oSettings._iDisplayStart = iStart;
            that.fnDraw( false );
        }
         
        that.oApi._fnProcessingDisplay( oSettings, false );
         
        /* Callback user function - for event handlers etc */
        if ( typeof fnCallback == 'function' && fnCallback != null )
        {
            fnCallback( oSettings );
        }
    }, oSettings );
}
