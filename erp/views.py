# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from erp.forms import LoginForm, RegisterForm
#from utilization.models import User
from django.contrib.auth.models import User
from django.conf import settings
import logging, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from django.template import RequestContext
import md5

from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required


logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('file')

engine = create_engine(settings.CONNECT_INFO,echo=True,encoding='euc-kr',convert_unicode=True)
Session = sessionmaker(engine)
session = Session()

@login_required
def home(request):
    return render_to_response('home.html',context_instance=RequestContext(request))

def register_view(requeset):
    return render_to_response('register.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        logging.debug('valid %s', form.is_valid())
        if form.is_valid():
            cd = form.cleaned_data
            logging.debug('cleand data %s', cd)
            userName = cd['userName']
            password = cd['password']
            confirm  = cd['confirm']
            email    = cd['email']
            firstName = cd['firstName']
            lastName  = cd['lastName']
            hobby     = cd['hobby']
            favoriteAnimal = ['favoriteAnimal']
            aggrement = cd['aggrement']

            user = User(username=userName, first_name=firstName, last_name= lastName)
            user.set_password(password)
            user.save()
            
            p = user.get_profile()
            
            p.accepted_eula = aggrement
            p.hobby = hobby
            p.favoriteAnimal = favoriteAnimal
            
            p.save()
                
    else:
        form = RegisterForm()
    
    
    if form.errors:
        return render_to_response('register.html',{'form' : form})
    else:
        #return HttpResponseRedirect(next)
        return render_to_response('home.html',context_instance=RequestContext(request,user))
    
def hello(request):
    return HttpResponse('hello')

def test(request):
    return render_to_response('common/test.html')