#coding=utf-8
from django.db import models
from ckeditor.fields import RichTextField

class lostthing_context(models.Model):
	lostthing_title = models.CharField('标题',max_length=50)
	lostthing_content = RichTextField(verbose_name='内容')
	createtime = models.DateTimeField(auto_now_add = True)
	class Meta:
		ordering = ['-createtime']
