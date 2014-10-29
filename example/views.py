# coding=utf-8
import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from example.models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User

from blog.models import context

import urllib2,urllib,simplejson

from django.core.paginator import Paginator, EmptyPage, InvalidPage  #分页

key = 1

def test(request):
    return render_to_response('post.html')

@csrf_exempt
def post(request):
    if request.method == 'POST':
        user = request.POST['user']
        print user
        return render_to_response('post.html', context_instance=RequestContext(request))
    return render_to_response('post.html', context_instance=RequestContext(request))

def listing(request):
    msg = Post.objects.all()
    paginator = Paginator(msg, 6)  # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    #form = RegistrationForm(request.POST)
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('example/post.html', {"msg": msg, 'contacts': contacts, 'form': form})

def msg_show(request, id=''):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    return render_to_response('msg_show.html', {'post': post, 'id': id})

#@login_required
def msg_post_page(request):
    if request.method == 'POST':

        return HttpResponseRedirect('/messageboard/')
    variables = RequestContext(request,{'form': form})
    return render_to_response('msg_post_page.html', variables)