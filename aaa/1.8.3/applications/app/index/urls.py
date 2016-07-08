from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

from app.com.urlprefix import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    
    #added by app
    ('^get-test/$', views.get_test),
    ('^post-test/$', views.post_test),
    url(r'^blog-types/$', views.BlogTypesView.as_view()),
    url(r'^blog-types/(?P<id>[0-9]+)/$', views.BlogTypeView.as_view()),
    url(r'^userinfo/$', views.UserInfoView.as_view()),
)

