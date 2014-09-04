#coding=utf-8

import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,Http404
from django.template import RequestContext
from django.views.generic import list_detail
from messageboard.forms import *
from messageboard.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from blog.models import blog_main

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage#分页

def listing(request):
    posts = blog_main.objects.all()
    paginator = Paginator(posts, 6) # Show 25 contacts per page

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

    return render_to_response('index.html', {"contacts": contacts, 'posts':posts, 'form':form})

def bloglist(request):
    blogs = blog_main.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})


def blog_show(request,id=''):
        
    try:
        blog = blog_main.objects.get(id=id)
    except MsgPost.DoesNotExist:
        raise Http404
    return render_to_response('blog.html',{'blog':blog, 'id':id})

def register_page(request):
    key = 1 
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

@login_required
def msg_post_page(request):
    if request.method=='POST':
        form = MsgPostForm(request.POST)
        if form.is_valid():
            newmessage = MsgPost(title=form.cleaned_data['title'],content=form.cleaned_data['content'],)
            newmessage.save()
        return HttpResponseRedirect('/main/')
    else:
        form=MsgPostForm()
    variables=RequestContext(request,{'form':form,'title':title, 'menu_list':menu_list, 'menu_context':menu_context})
    return render_to_response('msg_post_page.html',variables)
