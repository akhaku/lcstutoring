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

function matchEditHandlers() {
    $('table.data tbody tr td').dblclick(function() {
        console.log("Clicked on match " + $(this).parent().attr('id'));
        return false;
    });
}

function tutorEditHandlers(base_url) {
    $('table.data tbody tr td').dblclick(function() {
        var dialog = $('<div style="display:none" title="Edit Tutor"></div>').
        appendTo('body');
        var tutor_id = $(this).parent().attr('id');
        url = base_url+""+tutor_id+"/";
        dialog.load(url, function (responseText, textStatus, XMLHttpRequest) {
            dialog.dialog({
                modal: true,
                width: 800,
                close: function(event, ui) {
                    dialog.remove();
                }
            });
        });
        return false;
    });
}

function tuteeEditHandlers(base_url) {
    $('table.data tbody tr td').dblclick(function() {
        var dialog = $('<div style="display:none" title="Edit Tutee"></div>').
        appendTo('body');
        var tutee_id = $(this).parent().attr('id');
        url = base_url+""+tutee_id+"/";
        dialog.load(url, function (responseText, textStatus, XMLHttpRequest) {
            dialog.dialog({
                modal: true,
                width: 800,
                close: function(event, ui) {
                    dialog.remove();
                }
            });
        });
        return false;
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
