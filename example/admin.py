from django.contrib import admin
from ck.fields import CKEditor
from example.models import Post
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):
	
	list_display = ('title','datetime')
	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor(ck_attrs={'width':'auto'})},
}

admin.site.register( Post, ArticleAdmin )
