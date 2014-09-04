The field looks up for ckeditor using the CKEDITOR_PATH on your settings.py. If it doesn't find CKEDITOR_PATH, it uses {{MEDIA_URL}}/js/ckeditor/

OBS: CKEDITOR_PATH must be relative to your MEDIA_URL.

Only it. :)

To install:

Put the ck folder into your project, add 'ck' to your installed_apps.

For use:

from django import forms
from ck.fields import CKEditor

class TestForm(forms.Form):
    test = forms.CharField(widget=CKEditor)

Put the form.media somewhere on the top of your template (so Django adds the CKEditor js automatically).
And we're done.

Oh, wait! Do you want to customize CKEditor ? That's fine.

class TestForm(forms.Form):
    test = forms.CharField(widget=CKEditor(ck_attrs={'toolbar' : 'Basic', 'uiColor' : '#9AB8F3'}))

Ready to go again. (Django-CK also takes a look at the default language in your setttings.py, but if you like, you can also manually set the language attribute in ck_attrs)

For your convenience, we are shipping the latest CKEditor version at the date. Of course, this means that only this version is fully tested. (Only shipped in subversion).
