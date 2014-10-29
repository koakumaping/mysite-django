#coding=utf-8
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
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
    #url(r'^weixin$','weixin.views.weixin'),
    #url(r'^lznapp$','lznapp.views.apptest'),
    #url(r'^pxy$','pxyweixin.views.weixin'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^all/$','main.views.listing'),

    url(r'^main/register/$','main.views.register_page'),
    url(r'^main/register/success/$',TemplateView,{'template': 'register_success.html'}),
    url(r'^main/login/$',login),
    url(r'^main/logout/$',logout,{'next_page':'/main/login/'}), #退出后跳转到主页
    url(r'^main/password/change/$', password_change,{'template_name':'registration/password_change.html'}),
    url(r'^main/password/change/done/$', password_change_done,{'template_name':'registration/password_change_success.html'}),

    url(r'^messageboard/$', 'messageboard.views.listing'),
    url(r'^messageboard/post/$', 'messageboard.views.msg_post_page'),
    url(r'^messageboard/(?P<id>\d+)/$','messageboard.views.msg_show',name='msgdetail'),

	
    url(r'^bloglist/$','main.views.bloglist'),
    url(r'^blog/(?P<id>\d+)/$','main.views.blog_show',name='detailblog'),
    
    url(r'^employlist/$','employ.views.listing'),
    url(r'^employ/(?P<id>\d+)/$','employ.views.show_employ',name='detailemploy'),

    url(r'^suggestlist/$','suggestboard.views.listing'),
    url(r'^suggestboard/(?P<id>\d+)/$','suggestboard.views.show_suggestboard',name='detailsuggestboard'),
    
    url(r'^lostlist/$','lostthing.views.listing'),
    url(r'^lostthing/(?P<id>\d+)/$','lostthing.views.show_lostthing',name='detaillostthing'),

    #url(r'^accounts/login','accounts.views.login_view'),
    #url(r'^accounts/logout','accounts.views.logout_view'),
	
    url(r'^ckeditor/', include('ckeditor.urls')),
    
    url(r'^game/sjm','game.views.show_game_sjm'),

    url(r'^$', 'moblie.views.show_moblie_index', name='index'),
    url(r'^position/$', 'position.views.show_position'),

    url(r'^test/$', 'example.views.test'),
    url(r'^test/post/$', 'example.views.post', name='post'),

)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG is False:
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,
    }),
   )
urlpatterns += staticfiles_urlpatterns()
