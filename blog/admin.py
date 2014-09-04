from django.contrib import admin
from ck.fields import CKEditor
from blog.models import blog_main
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):
	
	list_display = ('blog_title','createtime')
	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor(ck_attrs={'width':'auto'})},
}

admin.site.register( blog_main, ArticleAdmin )
