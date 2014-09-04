#coding=utf-8
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login,logout
from django.contrib.auth.views import password_change,password_change_done


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weixin$','weixin.views.weixin'),
    #url(r'^lznapp$','lznapp.views.apptest'),
    url(r'^pxy$','pxyweixin.views.weixin'),

	#url(r'^main/$', 'messageboard.views.listing'),
	url(r'^main/register/$','main.views.register_page'),
	url(r'^main/register/success/$',RedirectView.as_view,{'template': 'register_success.html'}),
	url(r'^main/login/$',login),
	url(r'^main/logout/$',logout,{'next_page':'/main/login/'}), #退出后跳转到主页
	url(r'^main/password/change/$', password_change,{'template_name':'registration/password_change.html'}),
	url(r'^main/password/change/done/$', password_change_done,{'template_name':'registration/password_change_success.html'}),
	url(r'^main/post/$', 'main.views.msg_post_page'),
    url(r'^main/$','main.views.listing', name='home'),
	
	url(r'^bloglist/$','main.views.bloglist'),
	url(r'^blog/(?P<id>\d+)/$','main.views.blog_show',name='detailblog'),
	
	url(r'^accounts/login','accounts.views.login_view'),
	url(r'^accounts/logout','accounts.views.logout_view'),
	
	url(r'^ckeditor/', include('ckeditor.urls')),
)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
urlpatterns += staticfiles_urlpatterns()

