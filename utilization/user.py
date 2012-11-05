from django.shortcuts import render_to_response
from utilization.models import User, UserLogin
from django.core.paginator import Paginator
from django.conf import settings

import logging, os

logging.basicConfig(filename=os.path.join(settings.PROJECT_DIR,'log\\debug.txt'), level=logging.DEBUG)
#log = logging.getLogger("ex")

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
        
        users = User.objects.filter(user_name__icontains='STM')
        #users = User.objects.all()
        for user in users:
            userResult = []
            userResult.append(user)
            for i in range(1,13):
                userCount = UserLogin.objects.filter(user_id__exact=user, year__exact=year, month__exact=i)
                if userCount.count():
                    userResult.append(userCount)
                else:
                    userResult.append(0)   
                
            result.append(userResult)            

    
    
    paginator = Paginator(result, 10)
    
    
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
