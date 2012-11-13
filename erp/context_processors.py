'''
Created on 2012. 11. 13.

@author: stmkmk
'''
from django.conf import settings

def max_pages(context):
    return {'MAX_PAGES' : settings.MAX_PAGES }