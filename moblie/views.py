from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def show_moblie_index(request):

     return render_to_response('index.html')
