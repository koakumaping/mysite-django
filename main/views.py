#coding=utf-8

import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,Http404
from django.template import RequestContext
#from django.views.generic import list_detail
from django.views.generic.list import ListView
from messageboard.forms import *
from messageboard.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from blog.models import context

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage#分页
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.shortcuts import render_to_response,RequestContext


def listing(request):
    posts = context.objects.all()
    paginator = Paginator(posts, 10) # Show 25 contacts per page

# Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
        form = RegistrationForm(request.POST)
    except ValueError:
        page = 1 

    # If page request (9999) is out of range, deliver last page of results.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('all.html', {"contacts": contacts, 'posts':posts, 'form':form})


def bloglist(request):
    blogs = context.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})

@csrf_exempt
def blog_show(request,id=''):
        
    blog = context.objects.get(id=id)
    return render_to_response('blog.html',{'blog':blog, 'id':id }, context_instance=RequestContext(request))

def register_page(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'],
                                        email = form.cleaned_data['email'],
                                        password = form.cleaned_data['password1'])
        return HttpResponseRedirect('/main/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request,{'form':form,})
    return render_to_response('register.html',variables)

#@login_required
def msg_post_page(request):
    if request.method=='POST':
        form = MsgPostForm(request.POST)
        if form.is_valid():
            newmessage = MsgPost(title=form.cleaned_data['title'],content=form.cleaned_data['content'],)
            newmessage.save()
        return HttpResponseRedirect('/main/')
    else:
        form=MsgPostForm()
    variables=RequestContext(request,{'form':form})
    return render_to_response('msg_post_page.html',variables)
