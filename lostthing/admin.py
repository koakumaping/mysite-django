from django.contrib import admin
from ck.fields import CKEditor
from lostthing.models import lostthing_context
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):
	
	list_display = ('lostthing_title','createtime')
	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor(ck_attrs={'width':'auto'})},
}

admin.site.register( lostthing_context, ArticleAdmin )
