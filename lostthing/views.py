#coding=utf-8

import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,Http404
from django.template import RequestContext
#from django.views.generic import list_detail
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from lostthing.models import lostthing_context

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage#分页
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.shortcuts import render_to_response,RequestContext


def listing(request):
    posts = lostthing_context.objects.all()
    paginator = Paginator(posts, 6) # Show 25 contacts per page

# Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1 

    # If page request (9999) is out of range, deliver last page of results.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('all_lostthing.html', {"contacts": contacts, 'posts':posts})


@csrf_exempt
def show_lostthing(request,id=''):
        
    lostthing = lostthing_context.objects.get(id=id)
    return render_to_response('lostthing.html',{'lostthing':lostthing, 'id':id }, context_instance=RequestContext(request))
