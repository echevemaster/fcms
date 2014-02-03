from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'fcms.web.views.index', name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^auth/', 'fcms.web.views.auth', name='auth'),
                       url('', include('social.apps.django_app.urls',
                                       namespace='social')),
                       url(r'^logout/$', 'fcms.web.views.logout'),
                       url(r'profile/$', 'fcms.web.views.profile',
                           name='profile'),
                       url(r'^done/$', 'fcms.web.views.index', name='done'),
                       )
