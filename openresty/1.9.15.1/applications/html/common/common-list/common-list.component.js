'use strict';

// Register `common` component, along with its associated controller and template
angular.
module('commonList').
component('commonList', {
    templateUrl: '/common/common-list/common-list.template.html',
    controller: function CommonListController($routeParams) {
        /* if ($routeParams.access_token) {
            console.log('access_token store');
            console.log($routeParams.access_token);
            sessionStorage['oauth_access_token'] = $routeParams.access_token;
            var next = sessionStorage['next_href'];
            if(!(next === null)){
                window.location.href=sessionStorage['next_href'];
                sessionStorage['next_href']=null;
            }
        } */
        
        this.commons = [
            {
              name: 'aaabbbccc',
              snippet: 'Fast just got faster with Nexus S.'
            }, 
            {
              name: 'bbbaaaccc',
              snippet: 'The Next, Next Generation tablet.'
            }, 
            {
              name: 'cccbbbaaa',
              snippet: 'The Next, Next Generation tablet.'
            }, 
            {
              name: 'xxxoooxxx',
              snippet: 'The Next, Next Generation tablet.'
            }
        ];
    }
});
