'use strict';

// Register `authTest` component, along with its associated controller and template
angular.
module('authTest').
component('authTest', {
    templateUrl: '/index/auth-test/auth-test.template.html',
    controller: function PhoneListController($http) {
        var self = this;
        $http.get('/demoapp/1.0/app/blog-types/').then(function(response) {
            //self.blogTypes = response.data.slice(0, 10);
            self.blogTypes = response.data;
        });
    }
});

