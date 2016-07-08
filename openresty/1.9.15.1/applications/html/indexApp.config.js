'use strict';

indexAppModule.
constant('User_Portal_Domain','test.3927.com').
constant('AAA_MODULE_NAME','aaa').
constant('IndexApp_Client_ID','afVc1z822mZgiLHX2j94argDTQ1RnUIuZMxfJXTM').
constant('IndexApp_Redirect_Uri','https://test.3927.com/demoapp/otest/');

indexAppModule.
factory('httpOauth2Interceptor', ['$rootScope', '$log', '$routeParams', 'User_Portal_Domain', 'AAA_MODULE_NAME', 'IndexApp_Client_ID', 'IndexApp_Redirect_Uri',
function($rootScope, $log, $routeParams, User_Portal_Domain, AAA_MODULE_NAME, IndexApp_Client_ID, IndexApp_Redirect_Uri) {
    $log.debug('$log is here to show you that this is a regular factory with injection');
    
    var httpOauth2Interceptor = {
        request: function(config) {
            $log.debug('httpOauth2Interceptor-request');
            
            $log.debug("attampt to get oauth_access_token from sessionStorage");
            var oauth_access_token = sessionStorage['oauth_access_token'];
            $log.debug(oauth_access_token);
            
            //var path = $location.url();
            //var path = window.location.pathname;
            var url = config.url;
            $log.debug(url);
            if(oauth_access_token && url.indexOf("/1.0/") != -1) {
                $log.debug("oauth_access_token exist, and request url start with /1.0/, set it to api header");
                config.headers.Authorization = 'Bearer ' + oauth_access_token;
            }
            
            $rootScope.$on('$routeChangeSuccess', function() {
                // $routeParams should be populated here
                $log.debug($routeParams);
                if ($routeParams.access_token) {
                    $log.debug("get oauth_access_token and save to sessionStorage");
                    var oauth_access_token = $routeParams.access_token;
                    $log.debug(oauth_access_token);
                    sessionStorage['oauth_access_token'] = oauth_access_token;
                    
                    $log.debug("get next and redirect to next");
                    var next = sessionStorage['next'];
                    $log.debug(next);
                    if(!(next === null)){
                        window.location.href=next;
                        //$location.path(next);
                    } else {
                        var index_url = "https://" + User_Portal_Domain + "/";
                        window.location.href = index_url;
                    }
                }
            });
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
            } else {
                $log.debug('NOT 403 ERROR');
                $log.debug(res);
            }
            return res;
        }
      };

    return httpOauth2Interceptor;
}]);

indexAppModule.
config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.headers.common['Accept'] = 'application/json';
    $httpProvider.defaults.withCredentials = true;
    $httpProvider.interceptors.push('httpOauth2Interceptor');
}).
config(['$logProvider', function($logProvider){
    $logProvider.debugEnabled(true);
}]).
config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
        $locationProvider.hashPrefix('!');

        $routeProvider.
        when('/', {
            templateUrl: '/index.template.html',
        }).
        when('/auth-test', {
            template: '<auth-test></auth-test>'
        }).
        otherwise({
            redirectTo: '/'
        });
    }
]);

