'''
Created on 2012. 12. 6.

@author: stmkmk
'''
from django import forms

class NoticeForm(forms.Form):
    application = forms.IntegerField()
    program     = forms.IntegerField()
    unit        = forms.IntegerField(required=False)
    division    = forms.MultipleChoiceField(required=False)
    location    = forms.MultipleChoiceField(required=False)
    department  = forms.MultipleChoiceField(required=False)
    title       = forms.CharField()
    body        = forms.Textarea()
    toDate      = forms.DateField()
    fromDate    = forms.DateField()
    
    