'''
Created on 2012. 12. 6.

@author: stmkmk
'''
from notice.models import Notice
from django import forms

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
