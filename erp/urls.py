from django.conf.urls import patterns, url, include
from django.conf import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()


# Common Page
urlpatterns = patterns('',
                       url(r'^erp/$','erp.views.home'),
                       url(r'^erp/login/$','django.contrib.auth.views.login',{'template_name' : 'login.html'}),
                       url(r'^erp/logout/$','django.contrib.auth.views.logout',{'template_name' : 'logout.html'}),
                       url(r'^erp/register/$','erp.views.register_view'),
                       url(r'^erp/registerProcess/$','erp.views.register'),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^erp/test','erp.views.test'),
                       )
                       
# User Utilization
urlpatterns += patterns('utilization.user',
                       url(r'^erp/util/user/$','util_user'),
                       url(r'^erp/util/user/month_graph/$','month_graph'),
                       url(r'^erp/util/user/day_graph/$','day_graph'),
                       )

urlpatterns += patterns('notice.views',
                        url(r'erp/notice/register/$','register'),
                        )
                       

                       
    # Examples:
    # url(r'^$', 'erp.views.home', name='home'),
    # url(r'^erp/', include('erp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #  url(r'^admin/', include(admin.site.urls)),


#if settings.DEBUG:
    # static files (images, css, javascript, etc.)
'''  
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
'''
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}))