from django.contrib import admin
from ck.fields import CKEditor
from employ.models import employ_context
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):
	
	list_display = ('employ_title','createtime')
	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor(ck_attrs={'width':'auto'})},
}

admin.site.register( employ_context, ArticleAdmin )
