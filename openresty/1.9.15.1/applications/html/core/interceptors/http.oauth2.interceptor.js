'use strict';

angular.
module('core').
factory('httpOauth2Interceptor', ['$log', '$routeParams', 'User_Portal_Domain', 'AAA_MODULE_NAME', 'IndexApp_Client_ID', 'IndexApp_Redirect_Uri',
function($log, $routeParams, User_Portal_Domain, AAA_MODULE_NAME, IndexApp_Client_ID, IndexApp_Redirect_Uri) {
    $log.debug('$log is here to show you that this is a regular factory with injection');
    
    var httpOauth2Interceptor = {
        request: function(config) {
            $log.debug('httpOauth2Interceptor-request');
            if ($routeParams.access_token) {
                $log.debug("get access_token and save to sessionStorage");
                var access_token = $routeParams.access_token;
                $log.debug(access_token);
                sessionStorage['oauth_access_token'] = access_token;
                
                $log.debug("get next and redirect to next");
                var next = sessionStorage['next'];
                $log.debug(next);
                if(!(next === null)){
                    window.location.href=next;
                    //$location.path(next);
                }
            } else {
                $log.debug("attampt to get access_token from sessionStorage");
                var oauth_access_token = sessionStorage['oauth_access_token'];
                $log.debug(access_token);
                
                //var path = $location.url();
                var path = window.location.pathname;
                if(oauth_access_token && path.indexOf("/api/") != -1) {
                    $log.debug("access_token exist, and request path start with /api/, set it to api header");
                    config.headers.Authorization = 'Bearer ' + oauth_access_token;
                } 
            }
            return config;
        },

        requestError: function(config) {
                $log.debug('httpOauth2Interceptor-requestError');
                return config;
        },

        response: function(res) {
            $log.debug('httpOauth2Interceptor-response');
            $log.debug(res);
            return res;
        },

        responseError: function(res) {
            $log.debug('httpOauth2Interceptor-responseError');
            if(res.status == 403) {
                $log.debug('store next to sessionStorage and redirect to oauth login page');
                var next = window.location.href;
                //var next = $location.path();
                sessionStorage['next'] = next;
                $log.debug(next);
                var oauth_url = "https://" + User_Portal_Domain + "/" 
                + AAA_MODULE_NAME + "/oauth/authorize/?response_type=code&client_id="
                + IndexApp_Client_ID + "&redirect_uri=" + IndexApp_Redirect_Uri;
                $log.debug(oauth_url);
                var oauth_url = encodeURI(oauth_url);
                $log.debug(oauth_url);
                window.location.href = oauth_url;
            }
            return res;
        }
      };

    return httpOauth2Interceptor;
}]);

