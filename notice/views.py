# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def register(request):
    return render_to_response('notice/register.html')