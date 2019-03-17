from django import forms
from markdownx.fields import MarkdownxFormField


class EditArticle(forms.Form):
    myfield = MarkdownxFormField()
