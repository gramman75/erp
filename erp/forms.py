# -*- coding: euckr -*-
'''
Created on 2012. 11. 13.

@author: stmkmk
'''
from django import forms
import re, logging
from django.conf import settings
logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('file')



class LoginForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField()
    rememberMe = forms.CheckboxInput()
    
    def clean_userName(self):
        userName = self.cleaned_data['userName']
        if userName == '':
            raise forms.ValidationError("Input User Name")
        return userName
    '''
    def clean_password(self):
        password = self.cleaned_data['password']
        p = re.compile('^(?=([a-zA-Z]+[0-9]+[a-zA-Z0-9]*|[0-9]+[a-zA-Z]+[a-zA-Z0-9]*)$).{6,12}')
        m = p.match(password)       
        
        if m:
            pass
        else:
            raise forms.ValidationError('Password Error')
        
        return password
    '''
    
    