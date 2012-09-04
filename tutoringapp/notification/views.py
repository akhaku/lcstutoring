from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from notification.models import Notification
from tmsutil.decorators import ajax_login_required

MAX_NOTIFICATIONS = 10 # Max to show at one time
NOTIFICATION_OVERLAP = 2 # How many should overlap

@ajax_login_required
def view_notifications(request, start):
    start = int(start)
    is_next = True # are there more
    is_prev = start != 0 # are there previous
    prev_link = ""
    if is_prev:
        prev_link = reverse('notification.views.view_notifications',
                args=[max(start - MAX_NOTIFICATIONS, 0)])
    notifications = Notification.objects.order_by('-date_time')
    next_start = start + MAX_NOTIFICATIONS - NOTIFICATION_OVERLAP
    count = notifications.count()
    if next_start > count: is_next = False
    next_link = reverse('notification.views.view_notifications',
            args=[next_start,])
    notifications = notifications[start:(start+MAX_NOTIFICATIONS)]
    return render_to_response('notification/all_notifications.html', {
        'notifications': notifications,
        'is_prev' : is_prev,
        'is_next' : is_next,
        'prev_link' : prev_link,
        'next_link' : next_link,
        'start' : start,
        'end' : min((start+MAX_NOTIFICATIONS), count)
        }, context_instance=RequestContext(request))
