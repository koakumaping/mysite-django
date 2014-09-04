# coding=utf-8
from django.db import models


class Article( models.Model ):
	ail_title = models.CharField('标题',max_length=50)
	ail_text = models.TextField('内容')

