from django.core.urlresolvers import reverse
""" The replacements made for the templated emails """

def tutee_replace(response, tutee):
    response = response.replace('[cfname]', tutee.child_first_name)
    response = response.replace('[clname]', tutee.child_last_name)
    response = response.replace('[pemail]', tutee.email_address)
    response = response.replace('[pfname]', tutee.parent_first_name)
    response = response.replace('[plname]', tutee.parent_last_name)
    response = response.replace('[grade]', str(tutee.grade))
    response = response.replace('[hphone]', tutee.home_phone_number)
    response = response.replace('[cphone]', tutee.cell_phone_number)
    response = response.replace('[ssubjects]', tutee.subjects)
    return response

def tutor_replace(response, tutor):
    response = response.replace('[fname]', tutor.first_name)
    response = response.replace('[lname]', tutor.last_name)
    response = response.replace('[semail]', tutor.email_address)
    response = response.replace('[tyear]', str(tutor.grad_year))
    response = response.replace('[tphone]', tutor.phone_number)
    return response

def manual_replace(response):
    link = '<a href="%s" target="_blank">' % reverse(
            'tmsutil.views.download_manual', args=[])
    response = response.replace('[manual]', link)
    response = response.replace('[/manual]', '</a>')
    return response
