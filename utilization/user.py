from django.shortcuts import render_to_response
from utilization.models import User, UserLogin
#import logging

#logging.basicConfig(filename="/home/gramman75/debug.log", level=logging.INFO)
#log = logging.getLogger("ex")

# Create your views here.
def header(requeset):
    return render_to_response('common/header.html')

def nav(requeset):
    return render_to_response('common/nav.html')

def util_user(request):
    return render_to_response('userCount/user_content.html')

def util_user_search(request):
    return render_to_response('userCount/user_search.html')

def util_user_result(request):
    users =''
    if 'year' in request.POST and request.POST['year']:
        year = request.POST['year']
        
        users = User.objects.all()
        
    return render_to_response('userCount/user_result.html',{'users' : users})
        
    
        
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
