# -*- coding: euckr -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
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
import calendar
import pygal
import logging, os
from django.contrib.auth.decorators import login_required


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

@login_required
def util_user(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/erp/login/')
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
            form = UserSearchForm()
            logging.debug('form error %s' , form.errors)
            return HttpResponse('Error!')
        #logging.debug('username : %s ',  userName)
        
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
        #logging.debug('dept :  %s', dept)
        #logging.debug('loc : %s', loc)
        
        for login in logins:  
            result.append(login)
    else:
        form = UserSearchForm()
              
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
    '''
    logging.debug('currentPosition %s', currentPosition)
    logging.debug('lastGroup %s', lastGroup)
    logging.debug('prevStartNum %s', prevStartNum)
    logging.debug('nextStartNum %s', nextStartNum)
    logging.debug('hasPrevGroup %s', hasPrevGroup)
    logging.debug('hasNextGroup %s', hasNextGroup)
    logging.debug('max_pages %s', max_pages)
    logging.debug('paginator.num_pages %s',  paginator.num_pages)
    logging.debug('end page %s',  (lambda x : int((currentPosition * max_pages)) + 1 if hasNextGroup else paginator.num_pages))
    '''       
    return render_to_response('userCount/user_content.html',{'result' : paginator.page(page),
                                                            'month' : range(1,13),
                                                            'cond' : form,      
                                                            'hasPrevGroup' : hasPrevGroup,
                                                            'hasNextGroup' : hasNextGroup,
                                                            'prevStartNum' : prevStartNum,
                                                            'nextStartNum' : nextStartNum,
                                                            'currentPosition ' : currentPosition,
                                                            'pageRange' : range(int((currentPosition-1)*max_pages + 1), int((currentPosition * max_pages)+1) if hasNextGroup else paginator.num_pages + 1)
                                                            }
                                                           ,context_instance=RequestContext(request)
                              )
def month_graph(request):

    
    data ={}
    chartData =[]
    
    if 'userId' in request.GET and request.GET['userId']:
        userId = request.GET['userId']
        
        result = session.query( UserLogin.year, UserLogin.month, func.sum(UserLogin.counts).label('count')).filter(UserLogin.user_id == userId).group_by(UserLogin.year, UserLogin.month)
        user = session.query(User).filter(User.id == userId).one()
        for row in result:
            data[int(row.month)] = int(row.count)
        
        for month in range(1,13):
            try:
                value = data[month]
            except KeyError:
                value = 0
            
            chartData.append(value)
        
        line_chart = pygal.Line()
        
        line_chart.title = user.description
        line_chart.x_labels = map(str,range(1,13))
        line_chart.add('',chartData)
        
        return HttpResponse(line_chart.render(False))
    else:
        return  HttpResponse('No Data')   
            
def day_graph(request):
    data ={}
    chartData =[]
    
    if 'userId' in request.GET and request.GET['userId']:
        userId = request.GET['userId']
        year   = int(request.GET['year'])
        month  = int(request.GET['month'])
        
        result = session.query( UserLogin.year, UserLogin.month, UserLogin.day, UserLogin.counts.label('count'))\
                 .filter(UserLogin.user_id == userId, UserLogin.year==year, UserLogin.month==month)
                 
        user = session.query(User).filter(User.id == userId).one()
        for row in result:
            data[int(row.day)] = int(row.count)
        
        lastDay = calendar.monthrange(year, month)[1]
        
        for day in range(1,lastDay+1):
            try:
                value = data[day]
            except KeyError:
                value = 0
            
            chartData.append(value)
        
        line_chart = pygal.Line()
        
        line_chart.title = user.description
        line_chart.x_labels = map(str,range(1,lastDay+1))
        line_chart.add('Counts',chartData)
        
        return HttpResponse(line_chart.render(False))
    else:
        return  HttpResponse('No Data')                 
        
        
