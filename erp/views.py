# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from erp.forms import LoginForm
from utilization.models import User
from django.conf import settings
import logging, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import md5

logging.basicConfig(filename=os.path.join(settings.PROJECT_DIR,'log\\debug.txt'),\
                    level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',\
                    datefmt='%m-%d %H:%M')

engine = create_engine(settings.CONNECT_INFO,echo=True,encoding='euc-kr',convert_unicode=True)
Session = sessionmaker(engine)
session = Session()

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
            
            try:
                user = session.query(User).filter(User.user_name == userName,\
                                                  password == md5.md5(password).hexdigest()
                                                  ).one()
            except NoResultFound:
                user = User()
            except MultipleResultsFound:
                pass
            
    else:
        form = LoginForm()
    
    logging.debug('form error %s', form.errors )
    return render_to_response('login.html',{'form' : form})

def hello(request):
    return HttpResponse('hello')

def test(request):
    return render_to_response('common/test.html')