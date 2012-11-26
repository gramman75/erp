# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from erp.forms import LoginForm
from django.conf import settings
import logging, os

logging.basicConfig(filename=os.path.join(settings.PROJECT_DIR,'log\\debug.txt'),\
                    level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',\
                    datefmt='%m-%d %H:%M')

def home(request):
    return render_to_response('home.html')

def login(request):
    return render_to_response('login.html')

def loginProcess(request):
    logging.debug('request %s', request.method)
    if request.method == 'GET':
        form = LoginForm(request.GET)
        logging.debug('valid %s', form.is_valid())
        if form.is_valid():
            cd = form.cleaned_data
            userName = cd['userName']
            password = cd['password']
            remmemberMe = cd['rememberMe']
            
    else:
        form = LoginForm()
    
    logging.debug('form error %s', form.errors )
    return render_to_response('login.html',{'form' : form})

        
            
        
        
       

def hello(request):
    return HttpResponse('hello')

def test(request):
    return render_to_response('common/test.html')