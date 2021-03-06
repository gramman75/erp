# -*- coding: euckr -*-
'''
Created on 2012. 11. 13.

@author: stmkmk
'''
from django import forms
import re, logging
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('file')

class LoginForm(forms.Form):
    userName = forms.CharField()
    pw = forms.CharField()
    rememberMe = forms.CharField(required=False)
    next       = forms.CharField(required=False)
    
    def clean_userName(self):
        userName = self.cleaned_data['userName']
        logger.debug('username %s' , userName)
        
        pw = self.cleaned_data['pw']
        
        user = authenticate(username=userName, password=pw)
                
        if user is not None:
            if user.is_active:
                pass
            else:
                raise forms.ValidationError('This user is inactive')
        else:
            raise forms.ValidationError('ID or password is wrong')
        
        return userName
    
  
    
    '''
    def clean_userName(self):
        userName = self.cleaned_data['userName']
        if userName == '':
            raise forms.ValidationError("Input User Name")
        return userName
    '''
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
class RegisterForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField()
    confirm  = forms.CharField()
    email    = forms.EmailField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    hobby    = forms.CharField(required=False)
    favoriteAnimal = forms.CharField(required=False)
    aggrement = forms.CharField()
    
    ''' 
    def clean_password(self):
        password = self.cleaned_data['password']
        logging.debug('password %s', password)
        p = re.compile('^(?=([a-zA-Z]+[0-9]+[a-zA-Z0-9]*|[0-9]+[a-zA-Z]+[a-zA-Z0-9]*)$).{6,12}')
        m = p.match(password)       
        
        logging.debug('m %s', m)
        
        if m:
            pass
        else:
            raise forms.ValidationError("Password is too short (minimum is 6 characters) and doesn't match the confirmation")
        
        return password

    def clean_confirm(self):
        password = self.cleaned_data['password']
        confirm  = self.cleaned_data['confirm']
        
        if password != confirm:
            raise forms.ValidationError("Password doesn't match the confirmation")
        return confirm
    def clean_userName(self):
        userName =self.cleaned_data['userName']
        try:
            user = User.objects.get(username = userName)
        except User.DoesNotExist:
            user = None
        
        if user:
            raise forms.ValidationError("Username is already taken.")
        
        return userName
     '''       
        
        
        
        