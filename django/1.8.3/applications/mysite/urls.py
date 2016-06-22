from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework.authtoken import views as authtoken_views
from app import views as app_views

from django.contrib.auth.views import login
from django.views.decorators.csrf import csrf_protect,csrf_exempt




from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from com.urlprefix import *

# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
'''urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
)'''

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ('^'+URL_PREFIX+'/header/$', app_views.header),
    ('^'+URL_PREFIX+'/footer/$', app_views.footer),
    ('^'+URL_PREFIX+'$', app_views.index),
    
    ('^'+URL_PREFIX+'/jobcenter/$', app_views.jobcenter),
    ('^'+URL_PREFIX+'/cloudhost/$', app_views.cloudhost),    
    ('^'+URL_PREFIX+'/help/$', app_views.help),
    ('^'+URL_PREFIX+'/otest/$', app_views.otest),
    ('^'+URL_PREFIX+'/GalaxyManagerLogIn/$', app_views.GalaxyManager_LogIn),
    
    (r'^'+URL_PREFIX+'/login/$', csrf_exempt(login), {"template_name": "registration/login.html"}, 'login'),
    ('^'+URL_PREFIX+'/logout/$', app_views.logout_view),
    ('^'+URL_PREFIX+'/changepwd/$', app_views.changepwd),
    ('^'+URL_PREFIX+'/modpwd/$', app_views.modpwd),
    
    url(r'^'+URL_PREFIX+'/admin/', include(admin.site.urls)),
    #(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #(r'^api-token-auth/', authtoken_views.obtain_auth_token),
    # url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    #added by app
    #('^'+URL_PREFIX_1_0+'/app/', include('app.urls')),
    
    #url(r'^'+URL_PREFIX+'/', include(router.urls)),
    url(r'^'+URL_PREFIX+'/oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)



