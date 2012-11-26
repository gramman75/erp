'''
Created on 2012. 11. 13.

@author: stmkmk
'''
from django import forms

class LoginForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField()
    rememberMe = forms.CheckboxInput()
    
    def clean_userName(self):
        userName = self.cleaned_data['userName']
        if userName == '':
            raise forms.ValidationError("Input User Name")
        return userName
