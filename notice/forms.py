'''
Created on 2012. 12. 6.

@author: stmkmk
'''
from django import forms

class NoticeForm(forms.Form):
    application = forms.IntegerField()
    program     = forms.IntegerField()
    unit        = forms.MultipleChoiceField(required=False)
    division    = forms.MultipleChoiceField(required=False)
    location    = forms.MultipleChoiceField(required=False)
    department  = forms.MultipleChoiceField(required=False)
    title       = forms.CharField()
    body        = forms.CharField()
    toDate      = forms.DateField()
    fromDate    = forms.DateField()
    
    