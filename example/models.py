#coding=utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Post(models.Model):
	title = models.CharField(max_length = 30)
	content = RichTextField(verbose_name="内容")
	datetime = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ['-datetime']

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','datetime','user')