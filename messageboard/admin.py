from django.contrib import admin
from ck.fields import CKEditor
from messageboard.models import MsgPost
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):
	
	list_display = ('title','datetime')
	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor(ck_attrs={'width':'auto'})},
}

admin.site.register( MsgPost, ArticleAdmin )
