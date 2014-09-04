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

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#分页

menu_list = ['健康资讯', '健康百科', '健康购物', '关于我们']
menu_context = ['温馨提示', '健康新闻', '健康养生', '健康饮食','健康健身','健康瘦身','时令蔬菜','健康菜谱','公司介绍','公司申明']
title = '健康管理吧'

key = 1

def listing(request):
    posts = MsgPost.objects.all()
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
		blog = MsgPost.objects.get(id=id)
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
	variables = RequestContext(request,{'form':form, 'title':title, 'menu_list':menu_list, 'menu_context':menu_context, 'key':key})
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

#def main(request):
	
#	posts = MsgPost.objects.all()#get all records
#	return render_to_response('index.html',{'posts':posts, 'title':title, 'menu_list':menu_list, 'menu_context':menu_context, 'key':key})

#生成请求code的url
def get_code_url(self, crsf_token):
	auth_url = '%s?%s'%(self.code_url, urllib.urlencode({
									'response_type': 'code',
									'client_id': self.appid,
									'redirect_uri': self.redirect_url,
									'scope': self.scope,
									'state': crsf_token,
									}))
	return auth_url
#解析获取code
def get_code(self, request):
	return request.REQUEST.get('code')

def get_token_url(self, code):

	token_url = '%s?%s'%(self.token_url, urllib.urlencode({
									'grant_type': 'authorization_code',
									'client_id': self.appid,
									'client_secret': self.appkey,
									'code': code,
									'redirect_uri': self.redirect_url,
									}))
	return token_url

def get_token(self, code):
	token_url = self.get_token_url(code)
	req = urllib2.Request(token_url)
	resp = urllib2.urlopen(req)
	content = resp.read()
	access_token = urllib2.urlparse.parse_qs(content).get('access_token', [''])[0]
	return access_token 


def get_openid_url(self, token):
	openid_url = '%s?%s'%(self.openid_url, urllib.urlencode({
									'access_token': token,
								}))
	return openid_url

def get_openid(self, token):
	openid_url = self.get_openid_url(token)
	req = urllib2.Request(openid_url)
	resp = urllib2.urlopen(req)
	content = resp.read()
	content = content[content.find('(')+1:content.rfind(')')]
	data = simplejson.loads(content)
	return data.get('openid')

def save(self, request):
	username = self.cleaned_data.get("username")
	mail = self.cleaned_data["email"].strip().lower()
	openid = request.session.get('openid')
	company = request.session.get('company')
	company = Company.objects.get(company__iexact=company)
	if not (openid and company):
		return None
	new_user = self.create_user(username)
	#EmailAddress.objects.add_email(new_user, email)
	EmailAddress(user=new_user, email=email, verified=True, primary=True).save()
	#OpenId.objects.add_openid(new_user, openid, company)
	OpenId(user=new_user, openid=openid, company=company).save()
	return new_user
