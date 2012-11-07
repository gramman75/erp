'''
Created on 2012. 10. 26.

@author: gramman
'''

from django.contrib import admin
from django.db import models

Department = models.get_model('utilization','Department')
Location = models.get_model('utilization','Location')
Program = models.get_model('utilization','Program')
ProgramCount = models.get_model('utilization','ProgramCount')
ProgramCountDetail = models.get_model('utilization','ProgramCountDetail')
Responsibility = models.get_model('utilization','Responsibility')
User = models.get_model('utilization','User')
UserLogin= models.get_model('utilization','UserLogin')

admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Program)
admin.site.register(ProgramCount)
admin.site.register(ProgramCountDetail)
admin.site.register(Responsibility)
admin.site.register(User)
admin.site.register(UserLogin)

