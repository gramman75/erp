# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from erp.forms import LoginForm
from utilization.models import User
from django.conf import settings
import logging, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from django.template import RequestContext
import md5

from django.contrib.auth import authenticate, login, logout

logging.basicConfig(filename=os.path.join(settings.PROJECT_DIR,'log\\debug.txt'),\
                    level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',\
                    datefmt='%m-%d %H:%M')

engine = create_engine(settings.CONNECT_INFO,echo=True,encoding='euc-kr',convert_unicode=True)
Session = sessionmaker(engine)
session = Session()

def home(request):
    return render_to_response('home.html')

def login_view(request):
    return render_to_response('login.html')

def loginProcess(request):
    message =''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        logging.debug('valid %s', form.is_valid())
        if form.is_valid():
            cd = form.cleaned_data
            userName = cd['userName']
            password = cd['password']
            #remmemberMe = cd['rememberMe']
            '''
            try:
                user = session.query(User).filter(User.user_name == userName,\
                                                  User.password == md5.md5(password).hexdigest()
                                                  ).one()
            except NoResultFound:
                message ='ID or Passwor is wrong'
            except MultipleResultsFound:
                message = 'Contact System Admin.'
            '''
            user = authenticate(username=userName, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    message = 'This user is inactive'
            else:
                message = 'ID or password is wrong'
                
    else:
        form = LoginForm()
    
    
    if form.errors or message:
        return render_to_response('login.html',{'form' : form,
                                                'message' : message}
                               
                                  )
    else:
        return render_to_response('home.html',context_instance=RequestContext(request,user))

def logout_view(request):
    logout(request)
    return render_to_response('home.html')
def hello(request):
    return HttpResponse('hello')

def test(request):
    return render_to_response('common/test.html')