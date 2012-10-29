# Create your views here.
from django.shortcuts import render_to_response
from django.db  import models

def userCount(request):
    if 'year' in request.POST and request.POST['year']:
        v_year = request.POST['year']
        User = models.get_model('utilization','User')
        
        users = User.objects.all()
        for user in users:
            UserLogin = models.get_model('utilization','UserLogin')
            userLogin = users.objects.filter(user_id__exact(user), year__exact(v_year))
        return render_to_response('userCount/userCount.html',{'users' : users})
    else:
        return render_to_response('userCount/userCount.html',{'users' : None})
        
    