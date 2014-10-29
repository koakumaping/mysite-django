from django.contrib import admin
from ck.fields import CKEditor
from suggestboard.models import suggestboard_context
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):
	
	list_display = ('suggestboard_title','createtime')
	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor(ck_attrs={'width':'auto'})},
}

admin.site.register( suggestboard_context, ArticleAdmin )
