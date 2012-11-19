# -*- coding: euckr -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilization.models import  User, UserLogin, Department, Location
from django.template import RequestContext
from utilization.forms import UserSearchForm
from django.core.paginator import Paginator
from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import case
from sqlalchemy import func
from django.conf import settings
import math
import time

import logging, os



logging.basicConfig(filename=os.path.join(settings.PROJECT_DIR,'log\\debug.txt'), level=logging.DEBUG)
#log = logging.getLogger("ex")

engine = create_engine(settings.CONNECT_INFO,echo=True,encoding='euc-kr',convert_unicode=True)
Session = sessionmaker(engine)
session = Session()


# Create your views here.
def header(requeset):
    return render_to_response('common/header.html')

def nav(requeset):
    return render_to_response('common/nav.html')
'''
def util_user(request):
    return render_to_response('userCount/user_content.html')
'''
def util_user_search(request):
    return render_to_response('userCount/user_search.html')

def util_user(request):
    result =[]
    
    year = ''    
    page = 1
    userName = ''
    loc =''
    dept =''
    max_pages = settings.MAX_PAGES
    
    if 'year' in request.GET and request.GET['year']:
        form = UserSearchForm(request.GET)
        
        if form.is_valid():
            cd = form.cleaned_data
            year = cd['year']
            page = cd['page']
            userName = cd['userName']
            dept = cd['dept']
            loc  = cd['loc']
        else:
            logging.debug('form error %s' , form.errors)
            return HttpResponse('Error!')
        logging.debug('username : %s ',  userName)
        
        jan = func.sum(case([(UserLogin.month == 1,UserLogin.counts)],else_ = 0)).label('jan')
        feb = func.sum(case([(UserLogin.month == 2,UserLogin.counts)],else_ = 0)).label('feb')
        mar = func.sum(case([(UserLogin.month == 3,UserLogin.counts)],else_ = 0)).label('mar')
        apr = func.sum(case([(UserLogin.month == 4,UserLogin.counts)],else_ = 0)).label('apr')
        may = func.sum(case([(UserLogin.month == 5,UserLogin.counts)],else_ = 0)).label('may')        
        jun = func.sum(case([(UserLogin.month == 6,UserLogin.counts)],else_ = 0)).label('jun')        
        jul = func.sum(case([(UserLogin.month == 7,UserLogin.counts)],else_ = 0)).label('jul')
        aug = func.sum(case([(UserLogin.month == 8,UserLogin.counts)],else_ = 0)).label('aug')
        sep = func.sum(case([(UserLogin.month == 9,UserLogin.counts)],else_ = 0)).label('sep')
        oct = func.sum(case([(UserLogin.month == 10,UserLogin.counts)],else_ = 0)).label('oct')
        nov = func.sum(case([(UserLogin.month == 11,UserLogin.counts)],else_ = 0)).label('nov')
        dec = func.sum(case([(UserLogin.month == 12,UserLogin.counts)],else_ = 0)).label('dec')
                   
        #logins  = session.query( User.description, Department.department, Location.location, jan, feb, mar, apr,may,jun,jul,aug,sep,oct,nov,dec).outerjoin(UserLogin, Department, Location).filter(UserLogin.year == year, User.description.like('%'+userName+'%')).group_by(User.user_name,User.description, Department.department, Location.location)                  
        logins  = session.query( User, jan, feb, mar, apr,may,jun,jul,aug,sep,oct,nov,dec)\
                .join(UserLogin, Department, Location)\
                .filter(UserLogin.year == year, User.description.like('%'+userName+'%'),Department.department.like('%'+dept+'%'),Location.location.like('%'+loc+'%'))\
                .group_by(User.user_name,User.description, Department.department, Location.location)                  
        logging.debug('dept :  %s', dept)
        logging.debug('loc : %s', loc)
        
        for login in logins:            
            result.append(login)
        
    paginator = Paginator(result, 20, orphans=10)
    
    currentPosition = int(math.ceil(page/max_pages))
    lastGroup = int(math.ceil(paginator.num_pages/max_pages))
    prevStartNum = 0
    nextStartNum = 0
    
    
    if paginator.num_pages <= max_pages:
        hasPrevGroup = False
        hasNextGroup = False
        
    else:
        if currentPosition < lastGroup:
            hasPrevGroup = True
            hasNextGroup = True
            prevStartNum = int((currentPosition-1) * max_pages)
            nextStartNum = int(currentPosition * max_pages + 1)
        else:
            hasPrevGroup = True
            hasNextGroup = False
            prevStartNum = int(currentPosition * max_pages - 1)
    
    logging.debug('currentPosition %s', currentPosition)
    logging.debug('lastGroup %s', lastGroup)
    logging.debug('prevStartNum %s', prevStartNum)
    logging.debug('nextStartNum %s', nextStartNum)
    logging.debug('hasPrevGroup %s', hasPrevGroup)
    logging.debug('hasNextGroup %s', hasNextGroup)
    logging.debug('max_pages %s', max_pages)
    logging.debug('paginator.num_pages %s',  paginator.num_pages)
    logging.debug('end page %s',  (lambda x : int((currentPosition * max_pages)) + 1 if hasNextGroup else paginator.num_pages))
            
    return render_to_response('userCount/user_content.html',{'result' : paginator.page(page),
                                                            'month' : range(1,13),
                                                            'year' : year,
                                                            'page' : page,
                                                            'userName' : userName,
                                                            'loc' : loc,
                                                            'dept' : dept,
                                                            'hasPrevGroup' : hasPrevGroup,
                                                            'hasNextGroup' : hasNextGroup,
                                                            'prevStartNum' : prevStartNum,
                                                            'nextStartNum' : nextStartNum,
                                                            'currentPosition ' : currentPosition,
                                                            'pageRange' : range(int((currentPosition-1)*max_pages + 1), int((currentPosition * max_pages)+1) if hasNextGroup else paginator.num_pages + 1)
                                                            }
                                                           ,context_instance=RequestContext(request)
                              )
    

        
        
    #monthCount = {}
    #result ={}
    #users = fnd_user_c.objects.filter(user_name__contains ='STM')
    #users = fnd_user_c.objects.filter(fnd_logins_c__start_time__gt=('2012-09-27 00:00:00'),fnd_logins_c__login_type__exact='FORM')    
    #logins = FndLogins.objects.select_related().filter(start_time__gt=('2012-05-01 00:00:00'),login_type__exact='FORM').extra(select={"Month" : "to_char(START_time,'RRRRMM')"}).values('user_id','Month').annotate(cnt = Count('login_id'))
    '''
    if user_name :
        users = FndUser.objects.filter(end_date__isnull=True,user_name__icontains=user_name)
    else:
        users = FndUser.objects.filter(end_date__isnull=True)
        
    for user in users:
        monthCount = {}
        for i in range(1,13):            
            loginCount = FndLogins.objects.select_related().filter(start_time__gt='2012-01-01 00:00:00',start_time__month=i,login_type__exact='FORM',user_id__exact=user.user_id).count()
            monthCount[i] = loginCount
        result[user.user_name] = monthCount

    #log.exception(result)
    print result
    '''
    #return render_to_response('userCount/user_result.html',{'month' : range(1,13), 'result' : result })
