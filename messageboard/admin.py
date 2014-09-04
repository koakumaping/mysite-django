from django.contrib import admin
from ck.fields import CKEditor
from messageboard.models import blog_tt
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):
	
	list_display = ('ail_title','create_datetime')
	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor},
}

admin.site.register( blog_tt, ArticleAdmin )
