# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from notice.models import Application, Program, OperationUnit, Division
from notice.forms import NoticeForm
from utilization.models import Location, Department 


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging, os
from django.conf import settings

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('file')


engine = create_engine(settings.CONNECT_INFO,echo=True,encoding='euc-kr',convert_unicode=True)
Session = sessionmaker(engine)
session = Session()


@login_required
def register_view(request):
    
    apps = session.query(Application).order_by(Application.application_name)
    units = session.query(OperationUnit).order_by(OperationUnit.name)
    divisions = session.query(Division).order_by(Division.name)
    locations = session.query(Location).order_by(Location.location)
    departments = session.query(Department).order_by(Department.department)
  
    return render_to_response('notice/register.html',locals())

def register_save(request):
    #logger.debug('request %s', request)
    if request.GET['application'] and request.GET['program'] and request.GET['body']:
        form = NoticeForm(request.GET)
        
        if form.is_valid():
            cd = form.cleaned_data
            application = cd['application']
            program     = cd['program']
            unit        = cd['unit']
            division    = cd['division']
            location    = cd['location']
            department  = cd['department']
            title       = cd['title']
            body        = cd['body']
            fromDate    = cd['fromDate']
            toDate      = cd['toDate']
            
        logger.debug('form %s', form)
        
    return render_to_response('notice/register.html')
    

def ajax_program(request):
    if 'applicationId' in request.GET and request.GET['applicationId']:
        application_id = request.GET['applicationId']        
        programs = session.query(Program).filter(Program.application_id == application_id).order_by(Program.program_name)
    
    return render_to_response('notice/ajax_program.html',locals())
        
        
        
        
        
        
        
        
        
        
        
        