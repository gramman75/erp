# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from notice.models import Application, Program, OperationUnit, Division, Notice, Target
from notice.forms import NoticeForm
from utilization.models import Location, Department 


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

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
    if request.POST['application'] and request.POST['program'] and request.POST['body']:
        application = request.POST['application']
        program     = request.POST['program']
        units       = request.POST.getlist('unit')
        divisions   = request.POST.getlist('division')
        locations   = request.POST.getlist('location')
        departments = request.POST.getlist('department')
        title       = request.POST['title']
        body        = request.POST['body']
        fromDate    = request.POST['fromDate']
        toDate      = request.POST['toDate']
        userId      = request.user.id
        
        logger.debug('userId %s', request.user.id)
        
        logger.debug('application %s', application)
        logger.debug('program %s', program)
        logger.debug('unit %s', units)
        logger.debug('division %s', divisions)
        logger.debug('location %s', locations)
        logger.debug('department %s', departments)
        logger.debug('title %s', title)
        logger.debug('body %s', body)
        logger.debug('fromDate %s', fromDate)
        logger.debug('toDate %s', toDate)
        
        
        
        notice = Notice(program, fromDate, toDate, title, body,userId)
        session.add(notice)
        
        session.commit()
            
        noticeId = notice.notice_id
        
        logger.debug('noticeId %s', noticeId)
        
        for unit in units:
            target = Target(noticeId,'UNIT',unit)
            session.add(target)
        
        for division in divisions:
            target = Target(noticeId,'DIVISION',division)
            session.add(target)
        
        for location in locations:
            target = Target(noticeId,'LOCATION',location)
            session.add(target)
        
        for department in departments:
            target = Target(noticeId,'DEPARTMENT',department)
            session.add(target)
        
        session.commit()
                    
    #return render_to_response('home.html')
    script = '''
        <script>
            alert('Register Complete!');
            content_ajax('/erp/notice/register/');
        </script>
        '''
    #return HttpResponse(script)
    return render_to_response('home.html',{'script' : script })

def ajax_program(request):
    if 'applicationId' in request.GET and request.GET['applicationId']:
        application_id = request.GET['applicationId']        
        programs = session.query(Program).filter(Program.application_id == application_id).order_by(Program.program_name)
    
    return render_to_response('notice/ajax_program.html',locals())
        
def register_list(request):
    return render_to_response('notice/register_list.html')        
        
        
        
        
        
        
        
        
        
        