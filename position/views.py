from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def show_position(request):

     return render_to_response('position.html')
