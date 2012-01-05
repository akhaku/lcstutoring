$(document).ready(function() {
    $('.tutor-cand, .tutee-cand').draggable({
        helper: function(event) {
                    console.log($(event.target));
                return $(event.target).clone();
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
            console.log(ui.helper.html());
            $('span#'+which+'-selected').text(ui.helper.html());
            $('span#'+which+'-selected').attr('rel',ui.helper.attr('rel'));
        }
    });
});
