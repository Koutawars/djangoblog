from django import forms
from django.contrib import admin
from django.forms import Textarea

from .models import Entry, Comment

class EntryForm(forms.ModelForm):
    content = forms.CharField( widget=Textarea(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = Entry
        fields = '__all__'

class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    # fields = ['title', 'content']

admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment)