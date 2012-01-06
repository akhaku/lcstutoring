$(document).ready(function() {
    initMatchDragDrop();
});


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
