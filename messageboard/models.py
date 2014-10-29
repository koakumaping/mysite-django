#coding=utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class News(models.Model):
	title = models.CharField(max_length = 30)
	content=RichTextField(verbose_name="内容")

class MsgPost(models.Model):
	user = models.CharField(max_length = 12)
	email = models.EmailField(blank = True)
	title = models.CharField(max_length = 30)
	content = RichTextField(verbose_name="内容")
	datetime = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ['-datetime']

class MsgPostAdmin(admin.ModelAdmin):
	list_display = ('title','datetime','user')

#admin.site.register(MsgPost,MsgPostAdmin)


class blog_tt( models.Model ):
	ail_title = models.CharField('标题',max_length=50)
	ail_text = RichTextField(verbose_name="内容")
	create_datetime = models.DateTimeField(auto_now_add = True)

class Company(models.Model):
	company = models.CharField('company', max_length=20)
	def __unicode__(self):
		return self.company.decode('utf8')

class OpenId(models.Model):
	user = models.ForeignKey(User, verbose_name='用户')
	company = models.ForeignKey(Company, verbose_name='公司')
	openid = models.CharField('openid', max_length=100)
	def __unicode__(self):
		return u'%s, %s'%(self.user.username, self.company)
