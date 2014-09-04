from django.contrib import admin
from ck.fields import CKEditor
from cktest.models import Article
from django.db import models

class ArticleAdmin( admin.ModelAdmin ):

	formfield_overrides	= {
		models.TextField: {'widget' : CKEditor},
}

admin.site.register( Article, ArticleAdmin )
