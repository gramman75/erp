'''
Created on 2012. 11. 13.

@author: stmkmk
'''
from django import forms

class UserSearchForm(forms.Form):
    year     = forms.CharField()
    page     = forms.IntegerField()
    userName = forms.CharField(required=False)
    dept     = forms.CharField(required=False)
    loc      = forms.CharField(required=False)