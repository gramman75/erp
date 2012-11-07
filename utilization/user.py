from django.shortcuts import render_to_response
from utilization.models import  User, UserLogin, Department, Location
from django.core.paginator import Paginator
from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import case
from sqlalchemy import func
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

def util_user(request,page=1):
    result = []
    if 'year' in request.POST and request.POST['year']:
        year = request.POST['year']

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
                   
        time1 = time.time()
        logins  = session.query(User.user_name, User.description, jan, feb, mar, apr,may,jun,jul,aug,sep,oct,nov,dec).join(UserLogin).filter(UserLogin.year == year).group_by(User.user_name,User.description)                   
        logging.debug(time.time()-time1)
        for user in logins:            
            result.append(user)
                
    paginator = Paginator(result, 1000)
    
    
    logging.debug('paginator %s', paginator.page_range)
            
    return render_to_response('userCount/user_content.html',{'result' : paginator.page(page),
                                                            'month' : range(1,13)})
        
    
        
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
