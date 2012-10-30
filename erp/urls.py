from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^erp/$','erp.views.home'),
                       url(r'^erp/header/$','utilization.user.header'),
                       url(r'^erp/nav/$','utilization.user.nav'),                       
                       url(r'^erp/util/user/$','utilization.user.util_user'),
                       url(r'^erp/util/user/search/$','utilization.user.util_user_search'),
                       url(r'^erp/util/user/result/$','utilization.user.util_user_result'),

                       
    # Examples:
    # url(r'^$', 'erp.views.home', name='home'),
    # url(r'^erp/', include('erp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

#if settings.DEBUG:
    # static files (images, css, javascript, etc.)
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
