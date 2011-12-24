from django.shortcuts import render_to_response

def all_tutors(request):
    return render_to_response('all_tutors',{},);
